let mapleader=" "
inoremap jk <Esc>


"split resize
nnoremap <Leader>> 10<C-w>> 
nnoremap <Leader>< 10<C-w>< 

nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>

"Plug
nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>t :NERDTreeFind<CR>
nmap <Leader>p :Files<CR>
nmap <Leader>ag :Ag<CR>

map <Leader>ob :Buffers<cr>

nnoremap <C-j> 10<C-e>
nnoremap <C-k> 10<C-y>


"inoremap <silent><expr> <TAB>
"      \ coc#pum#visible() ? coc#pum#next(1) :
"      \ CheckBackspace() ? "\<Tab> :
"      \ coc#refresh()
"inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<C-h>

nmap <silent> gd <Plug>(coc-definition)
nmap <Leader>ac <Plug>(coc-codeaction-cursor)
imap <C-l> <Plug>(coc-snippets-expand)
vmap <C-j> <Plug>(coc-snippets-select)

"nvim dap
"noremap <Leader>dt :DapUiToggle<CR>
noremap <Leader>dt :lua require'dapui'.toggle()<CR>
noremap <Leader>db :DapToggleBreakpoint<CR>
noremap <Leader>dc :DapContinue<CR>
noremap <Leader>dn :DapStepOver<CR>
noremap <Leader>dr :lua require('dapui').open({reset = true})<CR>

"autopair
let g:AutoPairShortcutToggle=''

"Copilot
imap <silent> <M-s> <Plug>(copilot-suggest)
imap <silent> <M-d> <Plug>(copilot-dismiss)
imap <silent> <M-S> <Plug>(copilot-next)
imap <silent> <M-N> <Plug>(copilot-previous)
imap <silent> <M-l> <Plug>(copilot-accept-word)
nmap <silent> <Leader>asd :Copilot panel<CR>


