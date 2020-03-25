import colour
import os

input_path = os.path.dirname(__file__)
rgb_sd = colour.read_image(os.path.join(input_path, 'data', 'testImageSD.jpg'))
rgb_hd = colour.read_image(os.path.join(input_path, 'data', 'testImageHD.jpg'))
rgb_4k = colour.read_image(os.path.join(input_path, 'data', 'testImage4K.jpg'))

xyz_sd = colour.sRGB_to_XYZ(rgb_sd)
xyz_hd = colour.sRGB_to_XYZ(rgb_hd)
xyz_4k = colour.sRGB_to_XYZ(rgb_4k)

lab_sd = colour.XYZ_to_Lab(xyz_sd)
lab_hd = colour.XYZ_to_Lab(xyz_hd)
lab_4k = colour.XYZ_to_Lab(xyz_4k)

ycbcr_sd = colour.RGB_to_YCbCr(rgb_sd)
ycbcr_hd = colour.RGB_to_YCbCr(rgb_hd)
ycbcr_4k = colour.RGB_to_YCbCr(rgb_4k)


class sRGBtoXYZ:

    def time_sd(self):
        colour.sRGB_to_XYZ(rgb_sd)

    def time_hd(self):
        colour.sRGB_to_XYZ(rgb_hd)

    def time_4k(self):
        colour.sRGB_to_XYZ(rgb_4k)


class XYZtosRGB:

    def time_sd(self):
        colour.XYZ_to_sRGB(xyz_sd)

    def time_hd(self):
        colour.XYZ_to_sRGB(xyz_hd)

    def time_4k(self):
        colour.XYZ_to_sRGB(xyz_4k)


class RGBtoYCbCr:

    def time_sd(self):
        colour.RGB_to_YCbCr(rgb_sd)

    def time_hd(self):
        colour.RGB_to_YCbCr(rgb_hd)

    def time_4k(self):
        colour.RGB_to_YCbCr(rgb_4k)


class YCbCrtoRGB:

    def time_sd(self):
        colour.YCbCr_to_RGB(ycbcr_sd)

    def time_hd(self):
        colour.YCbCr_to_RGB(ycbcr_hd)

    def time_4k(self):
        colour.YCbCr_to_RGB(ycbcr_4k)


class XYZtoLab:

    def time_sd(self):
        colour.XYZ_to_Lab(xyz_sd)

    def time_hd(self):
        colour.XYZ_to_Lab(xyz_hd)

    def time_4k(self):
        colour.XYZ_to_Lab(xyz_4k)


class LabtoXYZ:

    def time_sd(self):
        colour.Lab_to_XYZ(lab_sd)

    def time_hd(self):
        colour.Lab_to_XYZ(lab_hd)

    def time_4k(self):
        colour.Lab_to_XYZ(lab_4k)
