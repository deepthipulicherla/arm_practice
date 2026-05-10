import json

def validate_fps(fps):
    data = json.load(open("baselines/vulken_rotate_triangle.json"))
    return fps >= data["fps"]

