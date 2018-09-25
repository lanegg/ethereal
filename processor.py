# coding=utf8
import cv2
import library
import data


def build_features(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()

    kp, des = sift.detectAndCompute(gray, None)

    return des

def save_all_features():
    covers = library.load_all_covers()

    for cover in covers:
        save_features(cover)

def save_features(img_path):
    des = build_features(img_path)
    data.albums[img_path] = des


def match(des_a, des_b):

    count = 0

    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des_a, des_b, k=2)
    # goodMatch = []
    for m, n in matches:
        if m.distance < 0.50 * n.distance:
            # goodMatch.append(m)
            count = count + 1
    # goodMatch = numpy.expand_dims(goodMatch, 1)
    # print(goodMatch)

    return count

def match_all(source):
    source_des = build_features(source)
    result = None
    result_count = 0


    for album in data.albums.keys():
        count = match(data.albums[album], source_des)
        if count > result_count:
            result_count = count
            result = album

    print 'result:' + result
    return result