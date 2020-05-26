{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'Image' object is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-bc8727d4abee>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     36\u001b[0m \u001b[0mimages\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mImage\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfromarray\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstate\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     37\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 38\u001b[1;33m \u001b[0mimages\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msave\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'my.gif'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msave_all\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mappend_images\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mimages\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moptimize\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mduration\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     39\u001b[0m \u001b[1;31m# AttributeError: 'NoneType' object has no attribute 'palette' could not solve this\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\ml\\lib\\site-packages\\PIL\\Image.py\u001b[0m in \u001b[0;36msave\u001b[1;34m(self, fp, format, **params)\u001b[0m\n\u001b[0;32m   2132\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2133\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2134\u001b[1;33m             \u001b[0msave_handler\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfilename\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2135\u001b[0m         \u001b[1;32mfinally\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2136\u001b[0m             \u001b[1;31m# do what we can to clean up\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\ml\\lib\\site-packages\\PIL\\GifImagePlugin.py\u001b[0m in \u001b[0;36m_save_all\u001b[1;34m(im, fp, filename)\u001b[0m\n\u001b[0;32m    497\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    498\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0m_save_all\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mim\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfilename\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 499\u001b[1;33m     \u001b[0m_save\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mim\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfilename\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msave_all\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    500\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    501\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\ml\\lib\\site-packages\\PIL\\GifImagePlugin.py\u001b[0m in \u001b[0;36m_save\u001b[1;34m(im, fp, filename, save_all)\u001b[0m\n\u001b[0;32m    508\u001b[0m         \u001b[0mim\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mencoderinfo\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"optimize\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mim\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mencoderinfo\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"optimize\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    509\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 510\u001b[1;33m     \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0msave_all\u001b[0m \u001b[1;32mor\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0m_write_multiple_frames\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mim\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpalette\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    511\u001b[0m         \u001b[0m_write_single_frame\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mim\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpalette\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    512\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\ml\\lib\\site-packages\\PIL\\GifImagePlugin.py\u001b[0m in \u001b[0;36m_write_multiple_frames\u001b[1;34m(im, fp, palette)\u001b[0m\n\u001b[0;32m    427\u001b[0m     \u001b[0mframe_count\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    428\u001b[0m     \u001b[0mbackground_im\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 429\u001b[1;33m     \u001b[1;32mfor\u001b[0m \u001b[0mimSequence\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mitertools\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mchain\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mim\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mim\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mencoderinfo\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"append_images\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    430\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mim_frame\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mImageSequence\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mIterator\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mimSequence\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    431\u001b[0m             \u001b[1;31m# a copy is required here since seek can still mutate the image\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'Image' object is not iterable"
     ]
    }
   ],
   "source": [
    "import  numpy as np\n",
    "from PIL import Image\n",
    "\n",
    "rule_gol = np.array([\n",
    "    False, # 0 neighbor\n",
    "    False, # 1\n",
    "    True, # 2\n",
    "    True, # 3\n",
    "    False, # 4\n",
    "    False, # 5\n",
    "    False, # 6\n",
    "    False, # 7\n",
    "    False # 8\n",
    "    ])\n",
    "\n",
    "evolution_steps = 200\n",
    "vector_size = 300\n",
    "\n",
    "# Random initial state\n",
    "state = np.random.choice([True, False], size = (vector_size,vector_size))\n",
    "\n",
    "# Store result for each evolution step\n",
    "images = [Image.fromarray(state)]\n",
    "\n",
    "\n",
    "for i in range(evolution_steps):\n",
    "    state = rule_gol[1*np.roll(state,-301)+\n",
    "                     1*np.roll(state,-300)+\n",
    "                     1*np.roll(state,-299)+\n",
    "                     1*np.roll(state,-1)+\n",
    "                     1*np.roll(state,1)+\n",
    "                     1*np.roll(state,299)+\n",
    "                     1*np.roll(state,300)+\n",
    "                     1*np.roll(state,301)]\n",
    "    \n",
    "images.append(Image.fromarray(state))\n",
    "\n",
    "images[0].save('my.gif', save_all=True, append_images=images[1], optimize=True, duration=10)\n",
    "# AttributeError: 'NoneType' object has no attribute 'palette' could not solve this"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Py3 ml",
   "language": "python",
   "name": "ml"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
