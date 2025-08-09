local dap = require('dap')
local dap_python = require('dap-python')
local dapui = require('dapui')


dapui.setup()
dap_python.setup('python')

dap.adapters.python = {
	type = 'executable';
	command = 'python';
	args = { '-m', 'debugpy.adapter' };
}

dap.configurations.python = {
	{
		type = 'python';
		request = 'launch';
		name = 'debug current file';
		program = '${fileDirname}/main.py';
		pythonPath = function()
      local venv = os.getenv('VIRTUAL_ENV')
      if venv then
        return venv .. '/bin/python'
      else
        return '/usr/bin/python'
      end
		end;
	},
	{
    name= "Pytest: Current File";
    type= "python";
    request= "launch";
    program = '/home/HipnoTanatos/.venvs/hermesenv/bin/pytest';
		args = {"-m", "pytest", "--maxfail=1", "--disable-warnings"};
    justMyCode = false;
    subProcess = true;
  },
	{
    type = 'python';
    request = 'launch';
    name = "Launch pytest";

    program = "/home/HipnoTanatos/.venvs/hermesenv/bin/python";  -- Usar python como ejecutable
    args = {"-m", "pytest"};
    justMyCode = false;
  },
}
--dap.configurations.python = {
--    {
--      name= "Pytest: Current File",
--      type= "python",
--      request= "launch",
--      module= "pytest",
--      program = '${file}',
--      console= "integratedTerminal",
--    },
--  }

dap.listeners.before.attach.dapui_config = function()
  dapui.open()
end
dap.listeners.before.launch.dapui_config = function()
  dapui.open()
end
dap.listeners.before.event_terminated.dapui_config = function()
  dapui.close()
end
dap.listeners.before.event_exited.dapui_config = function()
  dapui.close()
end
