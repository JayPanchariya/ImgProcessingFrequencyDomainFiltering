{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "outputs": [],
   "source": [
    "f = os.path.join(IMDIR, \"/Users/jayotsana/Documents/sem_2_labs/image_processing/tp3/images-2/Frequency/tower.jpg\") \n",
    "img= io.imread(f, as_gray=True)\n",
    "img = img.astype(float)\n",
    "nu, nv = img.shape\n",
    "\n",
    "print(\"size of img : \", img.shape)\n",
    "fft_=np.fft.fftshift(np.fft.fft2(img, s=(nu,nv)))\n",
    "\n",
    "idl=lowPass(nu, nv, nu, nv, Do =4, filter='ideal')\n",
    "plt.figure(figsize=(5, 4))\n",
    "plt.imshow(idl, cmap='gray')\n",
    "plt.show()\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
