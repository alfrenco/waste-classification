import streamlit as st
import numpy as np
from skimage import io
from skimage.transform import resize
from PIL import Image
import tensorflow as tf

#load model
model2 = tf.keras.models.load_model("model2.h5", compile=False)

# Membuat title
st.title('Waste Classification')


# Membuat Form
with st.form(key='form_parameters'):
    st.title("Organic or Non-Organic")
    uploaded_file = st.file_uploader("Choose a file", type=['jpg', 'png', 'jpeg'])
    
    st.markdown('---')
    submitted = st.form_submit_button('Predict')
    
if submitted:
    image = Image.open(uploaded_file)
    np_img = np.asarray(image)
    resized = resize(np_img, (128,128,3),anti_aliasing=True)
    x = np.expand_dims(resized, axis=0)
    images = np.vstack([x])
    classes = model2.predict(images)
    if classes[0][0] > 0.5:
        st.write('## Recycle')
    else:
        st.write('## Organic')
    st.image(resized)


