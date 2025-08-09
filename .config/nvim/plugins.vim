call plug#begin('~/.config/nvim/plugged')


"syntax
"Plug 'sheerun/vim-polyglot'

" status bar
"Plug 'maximbaz/lightline-ale'
"Plug 'itchyny/lightline.vim'

"typing
Plug 'windwp/nvim-autopairs'
Plug 'tpope/vim-surround'

"autocomplete
"Plug 'sirver/ultisnips'
Plug 'honza/vim-snippets'
Plug 'neoclide/coc.nvim', {'branch': 'release'}

"IDE
Plug 'easymotion/vim-easymotion'
Plug 'christoomey/vim-tmux-navigator'
Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'
Plug 'mhinz/vim-signify'
Plug 'yggdroot/indentline'
Plug 'tpope/vim-repeat'
Plug 'brenoprata10/nvim-highlight-colors'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'OXY2DEV/markview.nvim'

"Live-Server
Plug 'turbio/bracey.vim', {'do': 'npm install --prefix server'}

" Debugger
Plug 'mfussenegger/nvim-dap'

Plug 'theHamsta/nvim-dap-virtual-text'

Plug 'mfussenegger/nvim-dap-python'

Plug 'nvim-neotest/nvim-nio'
Plug 'rcarriga/nvim-dap-ui' 

"Themes
Plug 'gruvbox-community/gruvbox'
Plug 'shinchu/lightline-gruvbox.vim'

"File Browser
Plug 'scrooloose/NERDTree'

"Copilot
Plug 'github/copilot.vim'

call plug#end()
