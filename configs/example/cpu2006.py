#Mybench.py

import m5
from m5.objects import *
m5.util.addToPath('../common')

binary_dir = '/home/yeyong/yeyong/installspec2006/benchspec/CPU2006/'
data_dir = '/home/yeyong/yeyong/installspec2006/benchspec/CPU2006/'

process = LiveProcess()
def cpu2006(benchmark,process):
	if(benchmark == "perlbench"):
		#400
		process.executable = binary_dir+'400.perlbench/exe/perlbench_base.amd64-m64-gcc43-nn'
		data = data_dir + '400.perlbench/data/test/input/makerand.pl'
		process.cmd = [process.executable] + [data]
		return process
	elif(benchmark == "bzip2"):
		#401
		process.executable = binary_dir+'401.bzip2/exe/bzip2_base.amd64-m64-gcc43-nn'
		data = data_dir+'401.bzip2/data/all/input/input.program'
		process.cmd = [process.executable] + [data]
		return process
	elif(benchmark == "gcc"):
		#403
		process.executable = binary_dir+'401.bzip2/exe/bzip2_base.amd64-m64-gcc43-nn'
		data = data_dir+'403.gcc/data/test/input/cccp.i'
		process.cmd = [process.executable] + [data]
		return process
	elif(benchmark == "bwaves"):
		#410
		process.executable = binary_dir+'410.bwaves/exe/bwaves_base.amd64-m64-gcc43-nn'
		data = data_dir+'410.bwaves/data/test/input/bwaves.in' #the bwaves.in file should copy to the current (work) directory, if not, there will be a error
		process.cmd = [process.executable] + [data]
		return process
	elif(benchmark == "gamess"):
		#416 there is a error which is about out of memory 
		process.executable =  binary_dir+'416.gamess/exe/gamess_base.amd64-m64-gcc43-nn'
		process.input = data_dir+'416.gamess/data/test/input/exam29.config'
		process.cmd = [process.executable]
		return process
	elif(benchmark == "mcf"):
		#429.mcf
		process.executable = binary_dir+'429.mcf/exe/mcf_base.amd64-m64-gcc43-nn'
		data = data_dir+'429.mcf/data/test/input/inp.in'
		process.cmd = [process.executable] + [data]
		return process
	elif(benchmark == "milc"):
		#433.milc
		process.executable = binary_dir+'433.milc/exe/milc_base.amd64-m64-gcc43-nn'
		process.input = data_dir+'433.milc/data/test/input/su3imp.in'
		process.cmd = [process.executable]
		return process
	elif(benchmark == "zeusmp"):
		#434.zeusmp there is a error which is about out of memory
		process.executable = binary_dir+'434.zeusmp/exe/zeusmp_base.amd64-m64-gcc43-nn'
		process.cmd = [process.executable]
		return process
	elif(benchmark == "gromacs"):
		#435
		process.executable =  binary_dir+'435.gromacs/exe/gromacs_base.amd64-m64-gcc43-nn'
		data=data_dir+'435.gromacs/data/test/input/gromacs.tpr'
		process.cmd = [process.executable] + ['-silent','-deffnm',data,'-nice','0']
		return process
	elif(benchmark == "cactusADM"):
		#436
		process.executable =  binary_dir+'436.cactusADM/exe/cactusADM_base.amd64-m64-gcc43-nn'
		data=data_dir+'436.cactusADM/data/test/input/benchADM.par'
		process.cmd = [process.executable] + [data]
		return process
	elif(benchmark == "leslie3d"):
		#437
		process.executable =  binary_dir+'437.leslie3d/exe/leslie3d_base.amd64-m64-gcc43-nn'
		process.input=data_dir+'437.leslie3d/data/test/input/leslie3d.in'
		process.cmd = [process.executable]
		return process
	elif(benchmark == "namd"):
		#444
		process.executable =  binary_dir+'444.namd/exe/namd_base.amd64-m64-gcc43-nn'
		input=data_dir+'444.namd/data/all/input/namd.input'
		process.cmd = [process.executable] + ['--input',input,'--iterations','1','--output','namd.out']
		return process
	elif(benchmark == "gobmk"):
		#445
		process.executable =  binary_dir+'445.gobmk/exe/gobmk_base.amd64-m64-gcc43-nn'
		process.input=data_dir+'445.gobmk/data/test/input/capture.tst'
		process.cmd = [process.executable]+['--quiet','--mode','gtp']
		return process
	elif(benchmark == "dealII"):
		#447
		process.executable =  binary_dir+'447.dealII/exe/dealII_base.amd64-m64-gcc43-nn'
		process.cmd = [process.executable]+['8']
		return process
	elif(benchmark == "soplex"):
		#450
		process.executable =  binary_dir+'450.soplex/exe/soplex_base.amd64-m64-gcc43-nn'
		data=data_dir+'450.soplex/data/test/input/test.mps'
		process.cmd = [process.executable]+['-m10000',data]
		return process
	elif(benchmark == "povray"):
		#453
		process.executable =  binary_dir+'453.povray/exe/povray_base.amd64-m64-gcc43-nn'
		data=data_dir+'453.povray/data/test/input/SPEC-benchmark-test.ini'
		process.cmd = [process.executable]+[data]
		return process
	elif(benchmark == "calculix"):
		#454
		process.executable =  binary_dir+'454.calculix/exe/calculix_base.amd64-m64-gcc43-nn'
		data=data_dir+'454.calculix/data/test/input/beampic'
		process.cmd = [process.executable]+['-i',data]
		return process
	elif(benchmark == "hmmer"):
		#456
		process.executable =  binary_dir+'456.hmmer/exe/hmmer_base.amd64-m64-gcc43-nn'
		data=data_dir+'456.hmmer/data/test/input/bombesin.hmm'
		process.cmd = [process.executable]+['--fixed', '0', '--mean', '325', '--num', '5000', '--sd', '200', '--seed', '0', data]
		return process
	elif(benchmark == "sjeng"):
		#458
		process.executable =  binary_dir+'458.sjeng/exe/sjeng_base.amd64-m64-gcc43-nn'
		data=data_dir+'458.sjeng/data/test/input/test.txt'
		process.cmd = [process.executable]+[data]
		return process
	elif(benchmark == "GemsFDTD"):
		#459 the yee.dat file should copy to the current (work) directory, if not, there will be a error
		process.executable =  binary_dir+'459.GemsFDTD/exe/GemsFDTD_base.amd64-m64-gcc43-nn'
		process.cmd = [process.executable]
		return process
	elif(benchmark == "libquantum"):
		#462
		process.executable =  binary_dir+'462.libquantum/exe/libquantum_base.amd64-m64-gcc43-nn'
		process.cmd = [process.executable],'33','5'
		return process
	elif(benchmark == "h264ref"):
		#464
		process.executable =  binary_dir+'464.h264ref/exe/h264ref_base.amd64-m64-gcc43-nn'
		data=data_dir+'464.h264ref/data/test/input/foreman_test_encoder_baseline.cfg'
		process.cmd = [process.executable]+['-d',data]
		return process
	elif(benchmark == "lbm"):
		#470
		process.executable =  binary_dir+'470.lbm/exe/lbm_base.amd64-m64-gcc43-nn'
		data=data_dir+'470.lbm/data/test/input/100_100_130_cf_a.of'
		process.cmd = [process.executable]+['20', 'reference.dat', '0', '1' ,data]
		return process
	elif(benchmark == "omnetpp"):
		#471
		process.executable =  binary_dir+'471.omnetpp/exe/omnetpp_base.amd64-m64-gcc43-nn'
		data=data_dir+'471.omnetpp/data/test/input/omnetpp.ini'
		process.cmd = [process.executable]+[data]
		return process
	elif(benchmark == "astar"):
		#473
		process.executable =  binary_dir+'473.astar/exe/astar_base.amd64-m64-gcc43-nn'
		data = data_dir+'473.astar/data/test/input/lake.cfg'
		process.cmd = [process.executable]+[data]
		return process
	elif(benchmark == "wrf"):
		#481 the namelist.input file should copy to the current (work) directory, if not, there will be a error
		process.executable =  binary_dir+'481.wrf/exe/wrf_base.amd64-m64-gcc43-nn'
		data = data_dir + '481.wrf/data/test/input/namelist.input'
		process.cmd = [process.executable]+[data]
		return process
	elif(benchmark == "sphinx3"):
		#482
		#the ctlfile, args.an4 and beams.dat files should copy to the current (work) directory, if not, there will be a error
		process.executable =  binary_dir+'482.sphinx3/exe/sphinx_livepretend_base.amd64-m64-gcc43-nn'
		process.cmd = [process.executable]+['ctlfile', '.', 'args.an4']
		return process
	elif(benchmark == "xalancbmk"):
		#483
		process.executable =  binary_dir+'483.xalancbmk/exe/Xalan_base.amd64-m64-gcc43-nn'
		process.cmd = [process.executable]+['-v','test.xml','xalanc.xsl']
		return process
	elif(benchmark == "specrand_i"):
		#998
		process.executable = binary_dir+'998.specrand/exe/specrand_base.amd64-m64-gcc43-nn'
		process.cmd = [process.executable] + ['324342','24239']
		return process
	elif(benchmark == "specrand_f"):
		#999
		process.executable = binary_dir+'999.specrand/exe/specrand_base.amd64-m64-gcc43-nn'
		process.cmd = [process.executable] + ['324342','24239']
		return process
