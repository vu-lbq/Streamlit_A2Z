import streamlit as st
## similar to print function
# Title
st.title("This is our Title")
# Header
st.header("This is our Header")
st.header("This is a header with a divider", divider="gray")
# Sub-header
st.subheader("This is our Subheader")
# Caption
st.caption("This is our Caption")
st.write("Hello")
st.write('World!!!!')
# Text
st.text("This is some text.")
#Displaying Markdown
st.markdown("# Hi,\n# ***People*** \t!!!!!!!!!")
st.markdown('## Welcome to')
st.markdown("### Streamlit's World")

#Displaying Latex
st.latex(r'cos2\theta = 1 - 2sin^2\theta')
st.latex("(a+b)^2 = a^2 + b^2 + 2ab")
st.latex(r'''\frac{\partial u}{\partial t}
= h^2 \left( \frac{\partial^2 u}{\partial x^2}
+ \frac{\partial^2 u}{\partial y^2}
+ \frac{\partial^2 u}{\partial z^2} \right)''')