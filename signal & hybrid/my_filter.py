def my_imfilter(image, imfilter):

    '''
    Input:
        image: An array represent the input image.
        imfilter: The gaussian filter.
    Output:
        output: The filtered image.
    '''
    print(type(image))
    output = image.copy()
    im_dim=image.shape
    flt_dim=imfilter.shape
    img_dim1=im_dim[0]
    img_dim2=im_dim[1]
    flt_dim1=flt_dim[0]
    flt_dim2=flt_dim[1]
    
    #############Padding image before fitering####################
    
    pad_dim1=int((flt_dim1-1)/2)
    pad_dim2=int((flt_dim2-1)/2)
    #for gray scale
    if len(im_dim)==2:
        pad_mat=np.zeros((img_dim1+2*pad_dim1,img_dim2+2*pad_dim2))
        pad_mat[pad_dim1: img_dim1 + pad_dim1, pad_dim2: img_dim2 + pad_dim2] = image
                   
            ############    Gaussian filtering #############
    
        for i in range(len(image)):
                for j in range(len(image[0])):
                    output[i][j] = sum(sum(np.multiply(imfilter,pad_mat[i:i+flt_dim1,j:j+flt_dim2])))
        print('Input Image shape:',im_dim) 
        print('Filtered Image shape:',output.shape)
    
    #for RGB image
    else:
        pad_mat=np.zeros((img_dim1+2*pad_dim1,img_dim2+2*pad_dim2,im_dim[2]))
        pad_mat[pad_dim1: img_dim1 + pad_dim1, pad_dim2: img_dim2 + pad_dim2] = image
        
            ############    Gaussian filtering #############
    
        for d in range(len(image[0][0])):
            for i in range(len(image)):
                for j in range(len(image[0])):
                    output[i][j][d] = sum(sum(np.multiply(imfilter,pad_mat[i:i+flt_dim1,j:j+flt_dim2,d])))
        print('Input Image shape:',im_dim) 
        print('Filtered Image shape:',output.shape)

    ############    Gaussian filtering #############
    
#     for d in range(len(image[0][0])):
#         for i in range(len(image)):
#             for j in range(len(image[0])):
#                 output[i][j][d] = sum(sum(np.multiply(imfilter,pad_mat[i:i+flt_dim1,j:j+flt_dim2,d])))
#     print('Input Image shape:',im_dim) 
#     print('Filtered Image shape:',output.shape)
    return output