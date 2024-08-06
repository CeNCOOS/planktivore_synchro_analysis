import shutil
import glob
import os
import tqdm

def main():
    """
    Images are stored as .zip file with several different file types saves within the zip. We want to keep the pngs and jpgs
    """
    
    files = sorted(glob.glob("/opt/planktivore/*/*.zip"))
    
    print(f"Found {len(files)} zip files")
    
    remove_extensions = ["_binary.png","_edges.jpg","_edges.png","_ellipse.jpg","_ellipse.png","_original.tif"]
    for f in tqdm.tqdm(files):
        unpack_dir = os.path.join(os.path.abspath("."), "test_data")
        base_name = os.path.join(unpack_dir, os.path.basename(f).split(".zip")[0])
        shutil.unpack_archive(f, unpack_dir)
        [os.remove(base_name+ext) for ext in remove_extensions];
        
        try:
            shutil.move(base_name+"_rawcolor.jpg",os.path.join(unpack_dir,"jpgs"))
        except:
            os.remove(base_name+"_rawcolor.jpg")
        
        try:
            shutil.move(base_name+"_rawcolor.png",os.path.join(unpack_dir,"pngs"))
        except:
            os.remove(base_name+"_rawcolor.png")
        
        try:
            shutil.move(base_name+"_mask.png",os.path.join(unpack_dir,"masks"))
        except:
            os.remove(base_name+"_mask.png")


if __name__ == "__main__":
    main()