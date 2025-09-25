import streamlit as st
import os

st.set_page_config(layout='wide')

# Load MD blocks from assets/
def load_blocks():
    blocks = {}
    assets_dir = 'assets'
    if os.path.exists(assets_dir):
        for file in os.listdir(assets_dir):
            if file.endswith('.md'):
                with open(os.path.join(assets_dir, file), 'r') as f:
                    blocks[file] = f.read()
    return blocks

st.title('Prompt Builder')

blocks = load_blocks()

# Two columns: left for config, right for output (wider)
col1, col2 = st.columns([1, 2])

with col1:
    st.header('Configuration')
    selected_blocks = []
    for block_name in blocks.keys():
        if st.checkbox(f'Include {block_name}'):
            selected_blocks.append(block_name)

with col2:
    st.header('Output Prompt')
    
    with st.expander('Help'):
        st.write('The prompt file can be downloaded and then uploaded to the LLM app (using the upload file feature) for Grok, ChatGPT, Claude, or Gemini to have a dialogue with precise input data.')
    
    prompt = ''
    for block in selected_blocks:
        prompt += blocks[block] + '\n\n'
    
    # Download button at the top
    st.download_button(
        label='Download Prompt as MD',
        data=prompt,
        file_name='prompt.md',
        mime='text/markdown',
        key='download'
    )
    
    st.markdown(prompt)
