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
    "def plot_figure(img, x,y, fig, xlabel='s', ylabel='t', T = \"image\"):\n",
    "    nrow = 2\n",
    "    ncol = 2\n",
    "    dx, dy =0.04,0.04\n",
    "    w, h = (1/nrow)-dx , (1/ncol)\n",
    "    ax= fig.add_axes([x,y,w,h])\n",
    "    ax.imshow(img, cmap='gray')\n",
    "    ax.set_xlabel(xlabel)\n",
    "    ax.set_title(T)\n",
    "    \n",
    "def idelFilter(nu, nv, P, Q, Do):\n",
    "    lin_u = np.linspace(0,nu,nu)\n",
    "    lin_v = np.linspace(0,nv,nv)\n",
    "    u,v = np.meshgrid( lin_u ,   lin_v)\n",
    "    \n",
    "    dist =np.sqrt((u-P/2)**2 +  (v-Q/2)**2)\n",
    "    \n",
    "    mask = dist <= Do\n",
    "    \n",
    "    return mask.astype(int)\n",
    "    \n",
    "def lowPass(nu, nv, P, Q, Do =4, filter='ideal'):\n",
    "    if filter == 'ideal':\n",
    "        f=idelFilter(nu, nv, P, Q, Do)\n",
    "    return f\n",
    "\n",
    "def highPass(nu, nv, P, Q, Do =4, filter='ideal'):\n",
    "    if filter == 'ideal':\n",
    "        f=1-idelFilter(nu, nv, P, Q, Do)\n",
    "    return f"
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
