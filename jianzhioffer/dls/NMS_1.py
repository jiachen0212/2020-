# coding=utf-8
# https://github.com/hiJulie/NMS/blob/master/non_max_suppress.py
import numpy as np
import random
import cv2

def non_max_suppress(predicts_dict, thr):
    for object_name, bbox in predicts_dict.items():  # class and it's bbox: key, value
        bbox_array = np.array(bbox, dtype=np.float)
        x1 = bbox_array[:, 0]
        y1 = bbox_array[:, 1]
        x2 = bbox_array[:, 2]
        y2 = bbox_array[:, 3]
        scores = bbox_array[:, 4]
        order = scores.argsort()[::-1]   # 逆序排序score
        areas = (x2 - x1 + 1) * (y2 - y1 + 1)
        keep = []

        while order.size > 0:
            i = order[0]   # i 是box的编号
            keep.append(i)   # cur max's index
            # calue the iou:
            xx1 = np.maximum(x1[i], x1[order[1:]])   # x1[i] is the cur max, x1[order[1:]] is the other bbox
            yy1 = np.maximum(y1[i], y1[order[1:]])
            xx2 = np.minimum(x2[i], x2[order[1:]])
            yy2 = np.minimum(y2[i], y2[order[1:]])
            inter = np.maximum(0.0, xx2 - xx1 + 1) * np.maximum(0.0, yy2 - yy1 + 1)
            iou = inter / (areas[i] + areas[order[1:]] - inter)  # 广播机制
            inds = np.where(iou <= thr)[0]  # save the bbox if the iou <= thr
            order = order[inds + 1] #将order中的第inds+1处的值重新赋值给order；即更新保留下来的索引，加1是因为没有计算与自身的IOU，所以索引相差１，需要加上

        bbox = bbox_array[keep]
        predicts_dict[object_name] = bbox.tolist()
    return predicts_dict

