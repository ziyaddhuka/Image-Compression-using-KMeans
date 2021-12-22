import numpy as np
import pandas as pd
import os
from PIL import Image
import sys

if __name__ == '__main__':
    k = int(sys.argv[1])
    input_file_path = sys.argv[2]
    output_folder = sys.argv[3]
    img = Image.open(input_file_path)
    img_arr = np.asarray(img)
    orig_image_shape = img_arr.shape
    print(orig_image_shape)
    img_arr = img_arr.reshape(-1,3)


    file_sizes = []
    for lp in range(10):
        centroids = np.random.choice(range(img_arr.shape[0]-1), k, replace = False)
        centroids = img_arr[centroids].copy()
        lt = 0
        while lt<100:
            lt += 1
            flag = 0
            for centroid in centroids:
                euclid_dist_with_a_centriod = np.linalg.norm(img_arr-centroid, axis=1).reshape(-1,1)
                if flag == 0:
                    flag = 1
                    dist_ar = euclid_dist_with_a_centriod.copy()
                    continue
                dist_ar = np.hstack([dist_ar, euclid_dist_with_a_centriod])

            best_close_centriod = np.argmin(dist_ar, axis=1)
            prev_centriod = centroids.copy()
            centroids = []
            for i in range(k):
                if img_arr[np.where(best_close_centriod==i)].size == 0:
                    flag2 = 1
                    centroids.append(prev_centriod[i])
                    continue
                centroids.append(np.mean(img_arr[np.where(best_close_centriod==i)], axis=0))
            if np.allclose(prev_centriod, centroids, rtol=1e-02):
                break

        final_img = np.array(centroids)[best_close_centriod]
        final_img = final_img.astype('uint8')
        img = final_img.reshape(orig_image_shape)
        img = Image.fromarray(img)

        img.save('{}/out_{}_{}.jpg'.format(output_folder, k, lp))
        file_sizes.append(os.stat('{}/out_{}_{}.jpg'.format(output_folder, k, lp)).st_size)

    orig_image_size = os.stat(input_file_path).st_size
    # OLD FORMULA
    # compression_ratio = orig_image_size / np.array(file_sizes)
    # New_formula
    compression_ratio = np.array(file_sizes)/orig_image_size
    print("Mean compression ratio = ", np.mean(compression_ratio))
    print("Compression Ratio variance = ", np.var(compression_ratio))
    print(pd.DataFrame(compression_ratio, columns = ["K="+str(k)]))
