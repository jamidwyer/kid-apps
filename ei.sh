#!/bin/sh
cd /home/ubuntu/running-against-bot
if [pgrep -fc "python 2019-09-10-nc.py" &>/dev/null == 0]; then
	python 2019-09-10-nc.py # 2019-08-15
else
    echo "Process already running"
fi
if [pgrep -fc "python 2019-09-10-ny.py" &>/dev/null == 0]; then
	python 2020-11-03-ny.py # 2019-10-11
else
    echo "Process already running"
fi
if pgrep -f "python 2020-11-03-ia.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-ia.py # 2020-01-24
fi
if pgrep -f "python 2020-11-03-tn.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-tn.py # 2020-02-02
fi
if pgrep -f "python 2020-11-03-nc.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-nc.py # 2020-02-07
fi
if pgrep -f "python 2020-11-03-nh.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-nh.py # 2020-02-11
fi
if pgrep -f "python 2020-11-03-ma.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-ma.py # 2020-02-12
fi
if pgrep -f "python 2020-11-03-la.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-la.py # 2020-02-15
fi
if pgrep -f "python 2020-11-03-al.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-al.py # 2020-02-15
fi
if pgrep -f "python 2020-11-03-ca.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-ca.py # 2020-02-17
fi
if pgrep -f "python 2020-11-03-fl.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-fl.py # 2020-02-18
fi
if pgrep -f "python 2020-11-03-az.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-az.py # 2020-02-18
fi
if pgrep -f "python 2020-11-03-mn.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-mn.py # 2020-03-03
fi
if pgrep -f "python 2020-11-03-il.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-il.py # 2020-03-17
fi
if pgrep -f "python 2020-11-03-md.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-md.py # 2020-04-07
fi
if pgrep -f "python 2020-11-03-ky.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-ky.py # 2020-04-20
fi
if pgrep -f "python 2020-11-03-mt.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-mt.py # 2020-05-01
fi
if pgrep -f "python 2020-11-03-wa.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-wa.py # 2020-05-18
fi
if pgrep -f "python 2020-11-03-ok.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-ok.py # 2020-06-05
fi
if pgrep -f "python 2020-11-03-wy.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-wy.py # 2020-08-04
fi
if pgrep -f "python 2020-11-03-tx.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-tx.py # 2020-10-06
fi
if pgrep -f "python 2020-11-03-mi.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-mi.py # 2020-11-03
fi
if pgrep -f "python 2020-11-03-sc.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-sc.py # 2020-11-03
fi
if pgrep -f "python 2020-11-03-oh.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-oh.py # 2020-11-03
fi
if pgrep -f "python 2020-11-03-nj.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-nj.py # 2020-11-03
fi
if pgrep -f "python 2020-11-03-pa.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-pa.py # 2020-11-03
fi
if pgrep -f "python 2020-11-03-co.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-co.py # 2020-11-03
fi
if pgrep -f "python 2020-11-03-me.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-me.py # 2020-11-03
fi
if pgrep -f "python 2020-11-03-ms.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-ms.py # 2020-11-03
fi
if pgrep -f "python 2020-11-03-wv.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-wv.py # 2020-11-03
fi
if pgrep -f "python 2020-11-03-in.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-in.py # 2020-11-03
fi
if pgrep -f "python 2020-11-03-ut.py" &>/dev/null; then
    echo "Process already running"
else
	python 2020-11-03-ut.py # 2020-11-03
fi
