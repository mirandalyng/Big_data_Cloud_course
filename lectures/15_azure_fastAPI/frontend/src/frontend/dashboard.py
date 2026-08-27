import streamlit as st
import httpx
import os

BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")


# it is important to know url because in docker it will be seperated in containers
# behöver skicka en request till backend då det inte finns någon localhost

def main():
    st.markdown("# PokeDash")

    stats = httpx.get(f"{BASE_URL}/pokemons/stats",
                      timeout=30).json()
    st.dataframe(stats)


if __name__ == "__main__":
    main()
