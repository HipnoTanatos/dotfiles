set number 
set numberwidth=1
set relativenumber
set clipboard=unnamedplus
set showmatch
set sw=4
set noshowmode 
set mouse=a
set updatetime=300
set signcolumn=yes
set cursorline
set conceallevel=1
set foldmethod=expr
set foldexpr=nvim_treesitter#foldexpr()
set foldlevel=99
set foldtext=CustomFoldText()
set expandtab


so ~/.config/nvim/plugins.vim
so ~/.config/nvim/maps.vim
lua require('dap_config')
lua require('autopairs_config')
lua require('treesitter_config')
lua require('highlight_colors')

let g:gruvbox_sign_column = "none"
let g:gruvbox_number_column = "none"
let g:gruvbox_italic=1
let g:gruvbox_contrast_dark = "medium"
colorscheme gruvbox

let g:indentLine_char = '┊'

let NERDTreeQuitOnOpen=1

au BufRead,BufNewFile */templates/*.html,*/templates/**/*.html set filetype=htmldjango

let g:fzf_layout = { 'window': {  'width': 0.9, 'height': 0.6, 'border': 'sharp' } }
let g:fzf_color = {  }
" let g:fzf_layout = { 'down': '~60%' }
let g:fzf_vim = {}
let g:fzf_vim.preview_window = ['right,50%,sharp', 'ctrl-/']
let $FZF_DEFAULT_COMMAND='fd --type f --hidden --follow --exclude .git --exclude .obsidian --exclude .trash'

let g:copilot_enabled=0
let g:copilot_workspace_folders = ["~/Projects"]

let g:bracey_refresh_on_save = 1
let g:bracey_server_allow_remote_connections = 1

let g:python3_host_prog = '/usr/bin/python'
let g:ultisnips_python_style = "numpy"

highlight Normal ctermbg=none guibg=none

function! CustomFoldText()
	let line = getline(v:foldstart)
	let lines_count = v:foldend - v:foldstart + 1
	return line . ' ...        ' . lines_count . ' lines'
endfunction
