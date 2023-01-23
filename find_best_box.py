def find_probabilities_box(
    nums: list[int],
    target: float,
    current_sum: float,
    current_combo: list[float],
    combos: list[list[float]],
):
    if current_sum >= target:
        combos.append(current_combo)
        return

    if current_sum > target:
        return

    for i in range(len(nums)):
        find_probabilities_box(
            nums[i + 1 :],
            target,
            current_sum + nums[i],
            current_combo + [nums[i]],
            combos,
        )


def cube_volumes(total_volume: float, boxes: list[int]):
    used_boxes = list()
    boxes.sort(reverse=True)

    maneger_volumes = total_volume
    check_update_box: int = boxes[0]
    for index, box in enumerate(boxes):
        if check_update_box != box and boxes[-index] >= maneger_volumes > 0:
            used_boxes.append(boxes[-index])
            maneger_volumes -= boxes[-index]
            break

        while maneger_volumes >= box:
            if check_update_box != box:
                check_update_box = box
                break

            used_boxes.append(box)
            maneger_volumes -= box

    if maneger_volumes > 0:
        boxes.sort()
        combos = []
        find_probabilities_box(boxes, maneger_volumes, 0, [], combos)

        combos.sort(key=lambda x: len(x))
        closest_to_zero = min(combos, key=lambda x: abs(sum(x) - maneger_volumes))

        used_boxes.extend(closest_to_zero)

    return used_boxes


boxes = [10, 5, 20, 25, 30, 40, 60, 70, 90, 100, 386]
total_volume = 186
print(cube_volumes(total_volume, boxes), 186)
total_volume = 121
print(cube_volumes(total_volume, boxes), 121)
total_volume = 116
print(cube_volumes(total_volume, boxes), 116)
total_volume = 110
print(cube_volumes(total_volume, boxes), 110)
total_volume = 106
print(cube_volumes(total_volume, boxes), 106)
total_volume = 386
print(cube_volumes(total_volume, boxes), 386)
total_volume = 86
print(cube_volumes(total_volume, boxes), 86)
total_volume = 56
print(cube_volumes(total_volume, boxes), 56)
total_volume = 12
print(cube_volumes(total_volume, boxes), 12)
total_volume = 1.2
print(cube_volumes(total_volume, boxes), 1.2)
total_volume = 8
print(cube_volumes(total_volume, boxes), 8)
total_volume = 520
print(cube_volumes(total_volume, boxes), 520)
total_volume = 564
print(cube_volumes(total_volume, boxes), 564)
total_volume = 38
print(cube_volumes(total_volume, boxes), 38)
