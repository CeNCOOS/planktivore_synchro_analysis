import clustimage
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import glob
import matplotlib.pyplot as plt
import random
import numpy as np

def find_images():
    """Return a list of images with the relative directory to be clustered"""
    fnames = sorted(glob.glob("./test_data/pngs/*.png"))
    return fnames

def create_cluster_model(grayscale=True,resize=True,method='pca'):
    if resize:
        cl = clustimage.Clustimage(grayscale=grayscale, dim=(128,128),method=method,verbose=50)
    else:
        cl = clustimage.Clustimage(grayscale=grayscale,method=method,verbose=50)
    return cl

def run_cluster_model(cl, files, n_samples=10000,randomize=False):
    if randomize:
        random.shuffle(files)
        
    subsample = files[:n_samples]
    cl.fit_transform(subsample)
    return cl


def generate_plots(cl, experiment_name):
    plt.show(block=True)
    # Cluster Eval Plot (uses custeval API)
    save_name = os.path.join("./figures/",experiment_name+"_eval")
    fig, ax = cl.clusteval.plot(savefig={'fname':save_name,'dpi':300,'bbox_inches':'tight'})
    plt.clf()
    plt.close()
    # PCA Explaination PLot 
    fig,ax = cl.pca.plot(n_components=15,title=experiment_name)
    save_name = os.path.join("./figures/",experiment_name+"_pca.png")
    plt.savefig(save_name,dpi=300,bbox_inches='tight')
    plt.clf()
    plt.close()
    # Scatter TSNE Plot
    fig, ax = cl.scatter(dotsize=20, img_mean=False, plt_all=False)
    ax.set_title(f"{experiment_name}: TSNE Plot")
    save_name = os.path.join("./figures/",experiment_name+"_tsne.png")
    X = np.array(fig.canvas.renderer.buffer_rgba())
    plt.imsave(save_name,X)
    plt.clf()
    plt.close()
    # # Plot Unique - THis API doesn't return a figure
    # cl.plot_unique(img_mean=False)
    # save_name = os.path.join("./figures/",experiment_name+"_unique.png")
    # X = np.array(fig.canvas.renderer.buffer_rgba())
    # plt.imsave(save_name,X)
    # plt.close()


def main():
    files = find_images()
    print(f"Found {len(files)} images")
    
    save_name = "pca_20k_random_gray_resized"
    print(f"Experiment 1: {save_name}")
    cl = create_cluster_model(grayscale=True,resize=True, method='pca')
    cl = run_cluster_model(cl,files,n_samples=20000,randomize=True)
    cl.save(f"figures/cluster_models/{save_name}.pkl")
    generate_plots(cl, experiment_name=save_name)

    save_name = "pca_20k_random_gray_no_resized"
    print(f"Experiment 2: {save_name}")
    cl = create_cluster_model(grayscale=True,resize=False, method='pca')
    cl = run_cluster_model(cl,files,n_samples=20000,randomize=True)
    cl.save(f"figures/cluster_models/{save_name}.pkl")
    generate_plots(cl, experiment_name=save_name)
    
    save_name = "pca_20k_random_original_color_resized"
    print(f"Experiment 3: {save_name}")
    cl = create_cluster_model(grayscale=False,resize=False, method='pca')
    cl = run_cluster_model(cl,files,n_samples=20000,randomize=True)
    cl.save(f"figures/cluster_models/{save_name}.pkl")
    generate_plots(cl, experiment_name=save_name)

if __name__ == "__main__":
    main()