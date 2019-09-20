import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np
import math

dataset_hitogram = [188, 204, 181, 279, 200, 229, 281, 183, 174, 170, 341, 274, 271, 203, 174, 89, 226, 162, 252, 223, 239, 217, 163, 175, 262, 206, 264, 293, 236, 256, 252, 118, 251, 173, 126, 198, 263, 261, 244, 144, 191, 84, 166, 287, 187, 260, 208, 190, 283, 258, 267, 309, 156, 286, 277, 183, 163, 270, 285, 275, 217, 174, 219, 213, 197, 221, 251, 254, 248, 207, 160, 153, 195, 279, 123, 339, 287, 213, 186, 146, 193, 206, 163, 182, 225, 116, 287, 273, 159, 240, 229, 183, 247, 159, 174, 119, 129, 243, 256, 248, 224, 219, 302, 216, 270, 216, 133, 301, 310, 240, 213, 214, 110, 264, 236, 213, 294, 144, 207, 211, 229, 348, 321, 192, 82, 149, 108, 178, 197, 270, 224, 253, 271, 335, 210, 134, 170, 168, 165, 279, 119, 238, 291, 336, 130, 189, 162, 198, 140, 210, 201, 280, 210, 178, 209, 147, 193, 148, 206, 307, 183, 141, 331, 137, 229, 204, 212, 164, 257, 216, 216, 357, 224, 198, 227, 141, 184, 167, 284, 315, 59, 160, 131, 187, 261, 194, 220, 213, 158, 215, 173, 197, 215, 226, 209, 137, 140, 202, 298, 121, 204, 169, 193, 288, 98, 175, 274, 204, 216, 190, 215, 201, 173, 285, 243, 298, 180, 245, 187, 146, 165, 200, 232, 347, 248, 142, 167, 234, 242, 237, 177, 203, 194, 255, 251, 305, 185, 238, 161, 278, 217, 237, 214, 245, 189, 166, 197, 166, 244, 315, 268, 157, 100, 256, 282, 255, 193, 181, 233, 272, 163, 303, 174, 180, 80, 182, 231, 230, 295, 289, 214, 205, 254, 266, 270, 104, 153, 110, 290, 168, 168, 83, 217, 215, 226, 152, 101, 191, 232, 195, 126, 126, 260, 194, 226, 124, 246, 191, 158, 199, 130, 169, 167, 221, 186, 182, 374, 255, 242, 234, 224, 261, 142, 212, 151, 132, 146, 228, 142, 183, 174, 118, 284, 254, 183, 211, 102, 144, 285, 201, 192, 160, 133, 303, 307, 161, 232, 195, 241, 225, 149, 101, 197, 255, 136, 92, 155, 244, 303, 210, 250, 232, 200, 326, 207, 306, 260, 130, 215, 182, 237, 70, 238, 208, 60, 155, 162, 203, 128, 259, 281, 226, 182, 62, 103, 182, 176, 247, 282, 150, 149, 213, 154, 203, 165, 119, 251, 96, 224, 224, 183, 182, 159, 300, 124, 255, 134, 136, 133, 217, 248, 164, 164, 289, 202, 159, 219, 131, 226, 175, 212, 165, 238, 241, 307, 183, 174, 143, 167, 241, 241, 152, 165, 234, 113, 171, 203, 232, 266, 146, 250, 244, 169, 300, 51, 228, 132, 232, 191, 287, 363, 349, 346, 171, 282, 178, 226, 189, 169, 222, 211, 165, 209, 289, 238, 217, 213, 112, 97, 190, 181, 196, 172, 304, 106, 285, 158, 201, 283, 191, 314, 229, 107, 177, 270, 195, 218, 223, 128, 186, 190, 107, 365, 240, 206, 238, 216, 209, 185, 210, 150, 185, 136, 203, 165, 175, 210, 202, 211, 197, 203, 216, 186, 209, 209, 203, 203, 188, 199, 186, 200, 172, 213, 182, 163, 167, 177, 223, 141, 207, 200, 240, 237, 194, 199, 155, 190, 215, 203, 222, 195, 219, 196, 211, 185, 207, 169, 216, 198, 176, 194, 208, 171, 257, 269, 221, 193, 206, 211, 223, 291, 183, 233, 133, 210, 202, 159, 198, 139, 195, 188, 176, 67, 196, 181, 193, 208, 191, 164, 204, 217, 217, 132, 198, 253, 184, 191, 181, 204, 190, 193, 185, 179, 214, 187, 175, 114, 215, 163, 219, 130, 212, 139, 197, 255, 247, 233, 192, 229, 224, 186, 210, 178, 233, 197, 205, 223, 193, 202, 208, 194, 72, 164, 188, 192, 156, 95, 242, 147, 169, 201, 187, 172, 147, 205, 188, 226, 175, 119, 144, 212, 165, 164, 184, 165, 183, 163, 279, 193, 184, 208, 211, 233, 221, 205, 253, 168, 221, 182, 148, 159, 143, 182, 233, 190, 219, 180, 163, 168, 170, 190, 195, 218, 165, 237, 152, 228, 158, 224, 126, 224, 185, 195, 195, 170, 183, 184, 193, 172, 207, 139, 234, 127, 174, 222, 230, 187, 155, 179, 213, 177, 184, 224, 136, 227, 189, 197, 160, 95, 185, 184, 98, 154, 112, 178, 203, 132, 163, 195, 154, 194, 145, 163, 218, 194, 130, 162, 198, 243, 177, 221, 149, 251, 218, 199, 161, 184, 220, 229, 203, 181, 198, 180, 149, 204, 181, 186, 189, 207, 210, 206, 151, 189, 129, 221, 175, 184, 205, 207, 233, 186, 142, 96, 162, 182, 223, 209, 172, 178, 204, 206, 195, 164, 172, 195, 190, 188, 114, 195, 183, 172, 209, 205, 167, 155, 191, 144, 194, 255, 180, 110, 189, 194, 215, 243, 201, 184, 163, 149, 142, 211, 219, 211, 54, 223, 220, 191, 153, 134, 165, 148, 240, 131, 190, 219, 189, 158, 225, 156, 199, 119, 174, 150, 177, 273, 200, 198, 189, 222, 186, 164, 251, 218, 189, 133, 210, 196, 144, 224, 171, 186, 149, 218, 225, 180, 214, 257, 182, 185, 205, 188, 201, 207, 263, 185, 155, 178, 194, 163, 197, 216, 210, 196, 194, 224, 171, 221, 208, 192, 121, 225, 185, 191, 142, 133, 186, 174, 223, 135, 209, 154, 186, 180, 150, 190, 113, 194, 164, 151, 224, 180, 180, 222, 161, 181, 204, 245, 190, 176, 216, 175, 196, 161, 228, 163, 170, 49, 188, 219, 174, 206, 193, 178, 173, 155, 187, 143, 203, 213, 175, 202, 181, 186, 227, 159, 159, 185, 163, 196, 195, 148, 162, 141, 235, 201, 199, 186, 183, 231, 179, 138, 165, 183, 168, 90, 185, 205, 193, 153, 137, 204, 179, 185, 190, 187, 185, 166, 200, 197, 184, 182, 207, 233, 217, 220, 186, 203, 176, 239, 176, 162, 97, 113, 202, 147, 184, 150, 199, 194, 208, 226, 203, 214, 216, 209, 204, 104, 220, 146, 153, 130, 155, 197, 204, 235, 110, 174, 182, 212, 202, 197, 196, 184, 196, 181, 219, 207, 182, 212, 224, 251, 167, 191, 191, 183, 181, 178, 191, 150, 208, 242, 192, 177, 204, 204, 76, 183, 203, 200, 208, 192, 219, 147, 128, 197, 192, 187, 201, 166, 143, 183, 159, 122, 194, 178, 136, 90, 163, 181, 169, 172, 151, 176, 163, 71, 149, 145, 134, 119, 142, 176, 184, 131, 203, 162, 174, 167, 175, 125, 162, 141, 176, 133, 147, 119, 135, 60, 164, 209, 173, 159, 184, 193, 146, 59, 151, 164, 179, 144, 129, 41, 168, 153, 172, 180, 119, 130, 169, 163, 182, 197, 177, 95, 146, 187, 168, 187, 147, 156, 155, 207, 147, 214, 152, 194, 223, 124, 176, 158, 216, 134, 178, 118, 138, 210, 201, 158, 206, 172, 151, 178, 160, 188, 198, 189, 174, 153, 206, 129, 183, 158, 174, 175, 131, 144, 148, 200, 151, 201, 228, 111, 148, 199, 138, 184, 149, 201, 208, 190, 152, 151, 243, 105, 85, 160, 199, 147, 142, 197, 125, 210, 187, 160, 175, 152, 155, 154, 154, 171, 134, 143, 154, 201, 167, 197, 179, 128, 154, 190, 124, 179, 170, 155, 178, 185, 139, 126, 172, 207, 153, 180, 188, 189, 151, 207, 173, 227, 129, 152, 167, 138, 202, 197, 175, 173, 186, 190, 153, 235, 150, 158, 121, 154, 189, 174, 175, 141, 141, 189, 200, 115, 133, 172, 216, 184, 189, 169, 166, 175, 101, 142, 157, 195, 159, 169, 137, 137, 168, 189, 159, 166, 167, 124, 173, 155, 154, 200, 144, 220, 136, 208, 247, 208, 133, 105, 181, 194, 138, 158, 172, 124, 206, 197, 168, 163, 158, 206, 127, 192, 194, 166, 192, 147, 150, 172, 142, 159, 142, 135, 176, 142, 198, 173, 182, 179, 59, 170, 121, 153, 203, 158, 163, 158, 193, 117, 136, 189, 152, 126, 160, 167, 188, 165, 170, 157, 137, 153, 175, 104, 189, 164, 185, 156, 180, 199, 180, 198, 182, 140, 174, 191, 170, 151, 198, 128, 154, 150, 154, 184, 122, 158, 167, 151, 140, 151, 186, 138, 156, 171, 167, 133, 152, 141, 174, 171, 126, 185, 211, 176, 123, 209, 211, 191, 170, 213, 172, 143, 134, 238, 140, 141, 172, 126, 126, 194, 160, 190, 203, 187, 178, 148, 160, 190, 207, 144, 157, 177, 149, 178, 132, 191, 176, 145, 146, 143, 148, 171, 151, 163, 145, 151, 188, 194, 139, 165, 118, 144, 149, 189, 189, 160, 180, 187, 169, 172, 137, 146, 81, 111, 143, 76, 134, 182, 196, 187, 131, 190, 158, 185, 185, 166, 132, 124, 164, 143, 177, 89, 167, 167, 207, 196, 213, 193, 102, 123, 202, 143, 174, 173, 157, 142, 121, 158, 181, 151, 192, 145, 168, 184, 173, 145, 196, 162, 161, 136, 217, 173, 147, 169, 181, 215, 155, 159, 177, 188, 209, 100, 177, 191, 97, 173, 184, 152, 183, 177, 165, 57, 48, 140, 158, 202, 174, 156, 175, 123, 201, 100, 165, 181, 141, 175, 220, 138, 175, 147, 204, 175, 170, 146, 182, 180, 163, 172, 140, 203, 195, 194, 144, 155, 156, 207, 226, 180, 163, 149, 164, 151, 154, 147, 209, 170, 153, 162, 197, 159, 177, 183, 83, 159, 183, 150, 179, 204, 107, 229, 158, 203, 132, 135, 188, 133, 175, 194, 127, 211, 198, 137, 200, 167, 151, 173, 156, 123, 91, 176, 100, 162, 137, 133, 160, 167, 212, 155, 189, 152, 180, 178, 200, 149, 142, 133, 154, 207, 220, 239, 233, 278, 201, 186, 164, 279, 299, 211, 193, 238, 215, 182, 312, 263, 295, 206, 181, 240, 191, 192, 279, 224, 268, 313, 268, 214, 295, 239, 256, 92, 255, 309, 301, 302, 279, 350, 247, 245, 278, 221, 244, 288, 169, 277, 249, 291, 274, 279, 312, 281, 276, 245, 224, 266, 388, 363, 188, 275, 248, 90, 193, 222, 265, 252, 267, 234, 238, 316, 108, 285, 281, 242, 196, 205, 275, 288, 339, 261, 270, 287, 335, 245, 293, 74, 298, 253, 190, 229, 208, 334, 258, 285, 294, 123, 198, 376, 221, 172, 311, 325, 279, 180, 135, 260, 115, 127, 233, 190, 266, 297, 264, 277, 346, 265, 226, 255, 322, 285, 284, 245, 232, 199, 252, 371, 255, 115, 279, 230, 228, 263, 306, 244, 285, 229, 166, 242, 216, 256, 239, 226, 344, 288, 128, 272, 301, 225, 249, 237, 330, 260, 254, 99, 240, 337, 266, 218, 225, 255, 320, 278, 170, 218, 312, 216, 229, 313, 101, 104, 262, 311, 308, 245, 193, 251, 311, 272, 279, 360, 204, 137, 131, 241, 178, 288, 232, 311, 178, 248, 112, 255, 298, 219, 178, 205, 198, 251, 269, 292, 231, 230, 302, 248, 275, 223, 100, 203, 265, 113, 296, 326, 262, 299, 231, 122, 337, 255, 256, 310, 275, 247, 246, 242, 242, 273, 284, 290, 215, 240, 203, 225, 324, 272, 271, 252, 318, 270, 293, 294, 242, 264, 165, 116, 248, 255, 286, 315, 221, 350, 301, 252, 384, 256, 318, 292, 178, 259, 255, 341, 258, 318, 173, 254, 149, 258, 298, 224, 314, 200, 251, 217, 94, 300, 261, 241, 277, 283, 253, 310, 211, 289, 270, 271, 412, 293, 139, 308, 245, 279, 239, 290, 241, 218, 186, 253, 291, 292, 296, 303, 339, 255, 312, 270, 253, 306, 277, 288, 262, 262, 197, 177, 292, 344, 284, 304, 218, 174, 276, 284, 254, 265, 243, 234, 243, 297, 251, 316, 319, 384, 244, 252, 221, 231, 349, 220, 180, 293, 245, 240, 230, 333, 127, 146, 288, 311, 241, 217, 299, 247, 129, 228, 241, 325, 89, 210, 310, 308, 235, 286, 175, 290, 234, 311, 248, 312, 205, 217, 226, 264, 162, 236, 227, 235, 270, 236, 294, 299, 262, 229, 267, 258, 211, 234, 335, 283, 317, 234, 321, 261, 218, 298, 115, 250, 244, 290, 263, 297, 175, 193, 198, 278, 320, 311, 205, 307, 289, 240, 210, 222, 224, 280, 120, 243, 250, 216, 283, 213, 211, 308, 82, 269, 241, 301, 122, 275, 231, 219, 212, 282, 124, 225, 190, 261, 265, 270, 167, 330, 246, 259, 252, 244, 225, 246, 314, 251, 224, 133, 214, 222, 225, 355, 330, 250, 268, 308, 246, 281, 164, 155, 280, 142, 248, 131, 255, 213, 255, 319, 252, 226, 264, 233, 225, 304, 273, 275, 262, 184, 273, 185, 250, 280, 308, 239, 231, 198, 195, 238, 213, 286, 301, 268, 260, 256, 222, 274, 229, 303, 278, 278, 166, 180, 329, 293, 328, 219, 292, 256, 217, 259, 271, 305, 206, 178, 227, 311, 199, 86, 288, 300, 251, 315, 268, 110, 142, 264, 323, 217, 188, 248, 225, 208, 291, 287, 254, 240, 249, 250, 205, 313, 285, 127, 125, 236, 216, 305, 283, 133, 221, 213, 400, 242, 269, 223, 308, 226, 104, 216, 306, 305, 204, 214, 219, 181, 200, 255, 147, 235, 306, 294, 204, 229, 245, 213, 243, 265, 223, 308, 249, 277, 110, 303, 217, 188, 328, 264, 274, 269, 225, 217, 236, 278, 161, 253, 303, 252, 291, 281, 286, 263, 214, 287, 217, 294, 276, 285, 229, 227, 245, 224, 199, 253, 285, 211, 192, 272, 300, 234, 277, 135, 248, 348, 263, 266, 273, 218, 308, 242, 261, 251, 285, 231, 301, 260, 231, 177, 210, 256, 257, 285, 267, 265, 312, 263, 251, 184, 285, 255, 291, 249, 261, 237, 239, 56, 270, 304, 227, 262, 200, 240, 180, 254, 242, 390, 317, 211, 85, 245, 230, 244, 303, 237, 274, 175, 234, 265, 212, 352, 284, 248, 281, 318, 247, 254, 215, 317, 237, 181, 238, 231, 264, 213, 225, 375, 328, 131, 212, 304, 258, 293, 277, 214, 240, 208, 279, 237, 219, 258, 201, 139, 215, 248, 297, 279, 197, 229, 215, 286, 276, 52, 172, 109, 209, 223, 339, 274, 257, 235, 362, 227, 155, 288, 239, 211, 255, 234, 266, 269, 212, 166, 225, 281, 255, 384, 230, 218, 245, 271, 83, 251, 163, 269, 253, 251, 346, 141, 192, 291, 200, 265, 209, 156, 173, 319, 358, 244, 263, 320, 323, 132, 248, 198, 111, 176, 241, 246, 273, 272, 206, 251, 191, 242, 272, 137, 260, 291, 104, 260, 181, 214, 304, 257, 225, 241, 324, 308, 83, 232, 292, 187, 259, 273, 225, 240, 321, 204, 216, 335, 280, 327, 265, 267, 267, 255, 236, 268, 223, 317, 231, 239, 288, 205, 249, 237, 230, 353, 286, 196, 221, 240, 246, 322, 267, 285, 266, 331, 289, 212, 248, 225, 266, 234, 279, 155, 259, 254, 251, 156, 149, 219, 300, 314, 191, 231, 214, 230, 245, 189, 188, 261, 313, 364, 236, 203, 264, 153, 259, 309, 309, 212, 225, 243, 207, 217, 258, 235, 255, 197, 355, 202, 180, 422, 127, 294, 266, 324, 298, 282, 320, 325, 194, 214, 269, 240, 258, 279, 272, 276]
# plt.hist(dataset_hitogram, density=False, bins=100)
# plt.ylabel('Samples')
# plt.xlabel('Image size')
# plt.show()


def create_histogram(dataset, bins):
    dataset = np.array(dataset)
    dataset = dataset * 2
    max_ = max(dataset)
    min_ = min(dataset)
    range_ = (max_-min_)/bins

    histogram = np.zeros(bins)

    for i in dataset:

        index = int((i-min_-1)/range_)

        histogram[index] += 1

    axis = np.arange(bins)*range_+min_

    return axis, histogram


axis, data = create_histogram(dataset_hitogram,100)

for i in range(len(axis)):
    print(str(int(round(axis[i]))) + ',' + str(int(data[i])))


plt.bar(axis, data)
plt.ylabel('Samples')
plt.xlabel('Image size')
plt.show()