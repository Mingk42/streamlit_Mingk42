import streamlit as st
import numpy as np

iterations = st.sidebar.slider("level of detail", 2, 20, 10, 1)
separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)

progress_bar = st.sidebar.progress(0)

frame_text = st.sidebar.empty()
image = st.empty()

m, n, s = 960, 640, 400
x= np.linspace(-m / s, m / s, num=m).reshape((1,m))
y= np.linspace(-n / s, n / s, num=n).reshape((n,1))


for frame_num, a in enumerate(np.linspace(0.0, 4 * np.pi, 100)):
    progress_bar.progress(frame_num)
    frame_text.text(f'Frame {frame_num+1}/100')

    c = separation * np.exp(1j*a)
    Z = np.tile(x, (n,1)) * 1j * np.tile(y, (1,m))
    C = np.full((n,m),c)
    M = np.full((n,m), True, dtype=bool)
    N = np.zeros((n,m))

    for i in range(iterations):
        Z[M] = Z[M] * Z[M] + C[M]
        M[np.abs(Z)>2]=False
        N[M] = i

    image.image(1.0 - (N/N.max()), use_column_width=True)


progress_bar.empty()
frame_text.empty()

st.button("Re-run")
