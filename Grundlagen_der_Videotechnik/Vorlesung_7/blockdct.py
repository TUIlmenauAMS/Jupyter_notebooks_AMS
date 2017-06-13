
import scipy.fftpack as sft
import numpy as np

#Forward 8x8 DCT of type 2, orthogonal:
def dct8x8(frame):
    #Usage: X=dct8x8(frame)
    #2D DCT of blocks of 8x8 pixels of a 2D float array "frame" in array X.

    #First reshaping the image to width 8 and applying the 1D DCT all rows, then reshape it back,
    #then transpose it, and again reshape it to width 8 and apply the 1D DCT to each row, reshape it back,
    #and transpose it back.
    #with norm='ortho' for energy conservation in the subbands and for
    #invertibiltity without factor.
    #find the shape of "frame":
    [r,c]=frame.shape
    #First reshape frame as frame with rows of width 8, (rows: order= 'C' ),
    #and apply DCT to each row of length 8 of all blocks:
    frame=np.reshape(frame,(-1,8), order='C')
    X=sft.dct(frame,axis=1,norm='ortho')

    #shape it back to original shape:
    X=np.reshape(X,(-1,c), order='C')
    #Shape frame with columns of hight 8 by using transposition .T:
    X=np.reshape(X.T,(-1,8), order='C')
    X=sft.dct(X,axis=1,norm='ortho')

    #shape it back to original shape:
    X=(np.reshape(X,(-1,r), order='C')).T
    return X


#Inverse 2D DCT of type 2, orthogonal:
def invdct8x8(X):
    #Usage: x=invdct8x8(X)
    #with X: array of coefficients of 8x8 DCT's
    #x: reconstructed frame.

    #find the shape of
    [r,c]=X.shape
    #Rows:
    X=np.reshape(X,(-1,8), order='C')
    X=sft.idct(X,axis=1,norm='ortho')
    #shape it back to original shape:
    X=np.reshape(X,(-1,c), order='C')
    #Shape frame with columns of hight 8 (columns: order='F' convention):
    X=np.reshape(X.T,(-1,8), order='C')
    x=sft.idct(X,axis=1,norm='ortho')
    #shape it back to original shape:
    x=(np.reshape(x,(-1,r), order='C')).T
    return x

#Testing:
if __name__ == '__main__':
	import numpy as np

	frame=np.ones((16,16));
	print "frame= ", frame
	X=dct8x8(frame)
	print "dct8x8(frame)= ", X;
        x=invdct8x8(X)
	print "reconstructed x: ", x
