from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectSlider import DirectSlider
from direct.gui.DirectButton import DirectButton
from panda3d.core import (
    Point3,
    LineSegs,
    GeomLines,
    Geom,
    GeomNode,
    GeomVertexFormat,
    GeomVertexData,
    GeomVertexWriter,
    GeomTriangles,
)
import math
import numpy as np
from dataclasses import dataclass
from collada import Collada


@dataclass
class LidarConfig:
    num_of_layers: int
    vertical_angle_step: float
    horizontal_angle_step: float


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.lidar = LidarConfig(16, 0.4, 2.0)
        # self.disable_mouse()

        mesh = Collada("leg.dae")
        self.model_triangles = []
        mesh.scene
        for geometry in mesh.geometries:
            for primitive in geometry.primitives:
                trilist = list(primitive)

                for triangle in trilist:
                    tri = (triangle.vertices[0], triangle.vertices[1], triangle.vertices[2])
                    self.model_triangles.append(tri)
                    self.display_triangle(tri)

        self.camera.setPos(5.0, 10.0, 5)
        self.camera.lookAt(Point3(0, 0, 0))

        # Create a slider
        self.create_objects_sliders()
        self.create_lidar_sliders()
        self.create_and_display_grid()
        self.coordinates_text = OnscreenText(text="", pos=(0.1, -0.4), scale=0.05)

        self.taskMgr.add(self.updateCoordinatesTask, "update_coordinates_task")
        self.points = []
        self.slider_count = 0
        # self.tri_count = 0

    def display_triangle(self, triangle):
        # Create a new GeomVertexFormat
        format = GeomVertexFormat.getV3()

        # Create a new GeomVertexData
        vdata = GeomVertexData("triangle", format, Geom.UHStatic)

        # Create a GeomVertexWriter to write data into the GeomVertexData
        vertex_writer = GeomVertexWriter(vdata, "vertex")

        # Define the vertices of the triangle
        x, y, z = triangle[0]
        vertex_writer.addData3f(x, y, z)
        x, y, z = triangle[1]
        vertex_writer.addData3f(x, y, z)
        x, y, z = triangle[2]
        vertex_writer.addData3f(x, y, z)

        # Create a GeomTriangles object
        triangles = GeomTriangles(Geom.UHStatic)

        # Add vertices to the GeomTriangles object
        triangles.addVertices(0, 1, 2)

        # Create a Geom object
        geom = Geom(vdata)

        # Add the GeomTriangles object to the Geom
        geom.addPrimitive(triangles)

        # Create a GeomNode to hold the Geom
        geom_node = GeomNode("triangle")
        geom_node.addGeom(geom)

        # Create a NodePath with the GeomNode
        tr = self.render.attachNewNode(geom_node)
        tr.setColor(0.8, 0.5, 0.5, 1)
        # return

    def plot_points(self):
        self.clear_points()
        pointcloud = self.create_and_display_points_on_surface()
        # pointcloud = self.generate_pointcloud(self.lidar)
        # Display the points
        for position in pointcloud:
            self.points.append(self.create_and_display_points(position))

    def clear_points(self):
        for point in self.points:
            point.removeNode()

        self.points = []

    def create_and_display_grid(self):
        format = GeomVertexFormat.getV3()

        # Create a new GeomVertexData
        vdata = GeomVertexData("grid", format, Geom.UHStatic)

        # Create a GeomVertexWriter to write data into the GeomVertexData
        vertex_writer = GeomVertexWriter(vdata, "vertex")

        # Define the size and spacing of the grid
        grid_size = 10
        spacing = 1.0

        # Add horizontal lines to the grid
        for i in range(-grid_size, grid_size + 1):
            vertex_writer.addData3f(-grid_size * spacing, i * spacing, 0)
            vertex_writer.addData3f(grid_size * spacing, i * spacing, 0)

        # Add vertical lines to the grid
        for i in range(-grid_size, grid_size + 1):
            vertex_writer.addData3f(i * spacing, -grid_size * spacing, 0)
            vertex_writer.addData3f(i * spacing, grid_size * spacing, 0)

        # Create a GeomLines object
        lines = GeomLines(Geom.UHStatic)

        # Add vertices to the GeomLines object
        for i in range(vdata.getNumRows()):
            lines.addVertex(i)

        # Create a Geom object
        geom = Geom(vdata)

        # Add the GeomLines object to the Geom
        geom.addPrimitive(lines)

        # Create a GeomNode to hold the Geom
        geom_node = GeomNode("grid")
        geom_node.addGeom(geom)

    def _create_slider_in_right_down_corner(
        self, slider_range, position_z, callback, value=0, offset=0
    ):
        return DirectSlider(
            range=(-slider_range + offset, slider_range + offset),
            command=callback,
            pos=(0.8, 0, position_z),
            scale=0.5,
            value=value + offset,
        )

    def _create_slider_in_left_down_corner(
        self, slider_range, position_z, callback, value=0, offset=0
    ):
        return DirectSlider(
            range=(-slider_range + offset, slider_range + offset),
            command=callback,
            pos=(-0.6, 0, position_z),
            scale=0.5,
            value=value + offset,
        )

    def create_objects_sliders(self):
        self.slider_x = self._create_slider_in_right_down_corner(2, -0.45, self.updateSlider)
        self.slider_y = self._create_slider_in_right_down_corner(
            2, -0.55, self.updateSlider, 0, 16
        )
        self.slider_z = self._create_slider_in_right_down_corner(2, -0.65, self.updateSlider)

        self.slider_roll = self._create_slider_in_right_down_corner(180, -0.75, self.updateSlider)
        self.slider_pitch = self._create_slider_in_right_down_corner(180, -0.85, self.updateSlider)
        self.slider_yaw = self._create_slider_in_right_down_corner(180, -0.95, self.updateSlider)

    def create_lidar_sliders(self):
        self.slider_layers = self._create_slider_in_left_down_corner(
            256, -0.75, self.updateSlider, self.lidar.num_of_layers, 256 / 2
        )
        self.slider_v_step = self._create_slider_in_left_down_corner(
            5, -0.85, self.updateSlider, self.lidar.vertical_angle_step, 5 / 2
        )
        self.slider_h_step = self._create_slider_in_left_down_corner(
            5, -0.95, self.updateSlider, self.lidar.horizontal_angle_step, 5 / 2
        )

        self.button = DirectButton(
            text=("Render pointcloud", "Calculating...", "Render pointcloud"),
            scale=0.05,
            command=self.plot_points,
            pos=(-0.6, 0, -0.6),
        )

    def updateSlider(self):
        self.slider_count += 1
        if self.slider_count < 18:
            return
        # Update the model's position based on the slider value
        x = self.slider_x["value"]

        # self.dae_model.setPos(x,y,z)
        # self.dae_model.setHpr(roll,pitch,yaw)
        for triangle in self.model_triangles:
            triangle[0][0] = x

    def updateCoordinatesTask(self, task):
        # Update the 3D view coordinates text
        # pos = # self.dae_model.getPos()
        # hpr = # self.dae_model.getHpr()
        # self.coordinates_text.setText(f"\t\t\t\tModel Position: {pos}\nx: {pos.x}\n\ny: {pos.y}"
        #                               f"\n\nz: {pos.z}\n\nroll: {hpr.x}\n\npitch: {hpr.y}\n\nyaw: {hpr.z}")
        return task.cont

    def create_point_from_angles_and_range(self, v, h, r):
        point = Point3()
        point.x = r * math.cos(math.radians(h)) * math.cos(math.radians(v))
        point.y = r * math.cos(math.radians(h)) * math.sin(math.radians(v))
        point.z = r * math.sin(math.radians(h))
        return point

    def create_line_from_angles(self, v, h):
        versor = self.create_point_from_angles_and_range(v, h, 1.0)
        return versor

    def cross_surface_and_line(self, line, sufrace):
        x0, y0, z0 = (0, 0, 0)
        a, b, c = line
        A, B, C, D = sufrace
        div = A * a + B * b + C * c
        if div == 0:
            return None
        t = (-D - A * x0 - B * y0 - C * z0) / div
        x_przeciecia = x0 + a * t
        y_przeciecia = y0 + b * t
        z_przeciecia = z0 + c * t

        return x_przeciecia, y_przeciecia, z_przeciecia

    def make_surface_from_triangle(self, triangle):
        p1, p2, p3 = triangle
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        x3, y3, z3 = p3

        A = (y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1)
        B = (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1)
        C = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
        D = -A * x1 - B * y1 - C * z1
        return A, B, C, D

    def is_point_inside_triangle(self, point, triangle):
        A, B, C = triangle
        A = np.array(A)
        B = np.array(B)
        C = np.array(C)
        P = np.array(point)
        A = A - P
        B = B - P
        C = C - P

        u = np.cross(B, C)
        v = np.cross(C, A)
        w = np.cross(A, B)

        return np.dot(u, v) > 0 and np.dot(u, w) > 0

    def generate_pointcloud(self, lidar: LidarConfig):
        start_horizontal_angle = -lidar.num_of_layers * lidar.horizontal_angle_step / 2
        start_vertical_angle = 45.0
        num_of_vertical_points = int(90 / lidar.vertical_angle_step)
        points = []
        print(f"Num of layers: {lidar.num_of_layers}")
        for i in range(lidar.num_of_layers):
            h = start_horizontal_angle + i * lidar.horizontal_angle_step
            for j in range(num_of_vertical_points):
                v = start_vertical_angle + j * lidar.vertical_angle_step
                point = self.create_point_from_angles_and_range(v, h, 3.0)
                # self.create_and_display_edges([(0,0,0), point])
                points.append(point)
        return points

    def create_and_display_points_on_surface(self):
        points = self.generate_pointcloud(self.lidar)
        cross_points = []
        for point in points:
            cross_points_for_one_point = []
            for triangle in self.model_triangles:
                suface = self.make_surface_from_triangle(triangle)
                cross_point = self.cross_surface_and_line(point, suface)
                if cross_point is not None and self.is_point_inside_triangle(
                    cross_point, triangle
                ):
                    cross_points_for_one_point.append(cross_point)

            if len(cross_points_for_one_point) == 0:
                continue

            closest_point = (10000, 10000, 10000)
            for cross_point in cross_points_for_one_point:
                x_m, y_m, z_m = closest_point
                x, y, z = cross_point
                d_m = x_m * x_m + y_m * y_m, z_m * z_m
                d = x * x + y * y, z * z
                if d < d_m:
                    closest_point = cross_point

            cross_points.append(closest_point)
        # print(cross_points)
        return cross_points

    def create_and_display_edges(self, points):
        # Create edges between the points
        line_segs = LineSegs()
        line_segs.setColor(1, 1, 1, 1)

        for i in range(len(points) - 1):
            line_segs.moveTo(points[i][0], points[i][1], points[i][2])
            line_segs.drawTo(points[i + 1][0], points[i + 1][1], points[i + 1][2])

        line_node = line_segs.create()
        return self.render.attachNewNode(line_node)

    def create_and_display_points(self, position):
        # Create a point at the specified position
        point = self.loader.loadModel("models/smiley")
        point.setScale(0.01)  # Adjust the scale of the point
        point.setPos(Point3(*position))
        point.reparentTo(self.render)
        return point


app = MyApp()
app.run()
