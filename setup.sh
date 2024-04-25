#mkdir -p ~/.streamlit/
#
## shellcheck disable=SC2028
#echo "\
#[general]\n\
#email = \"gabriel.archilla1@upr.edu\"\n\
#" > ~/.streamlit/credentials.toml
#
## shellcheck disable=SC2028
#echo "\
#[server]\n\
#headless = true\n\
#enableCORS=false\n\
#port = $PORT\n\
#" > ~/.streamlit/config.toml

mkdir -p ~/.streamlit/
# shellcheck disable=SC2028
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml