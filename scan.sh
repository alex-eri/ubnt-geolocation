iwlist scan > /tmp/iwlist.scan
cat /tmp/iwlist.scan | grep Address | cut -d \  -f15 > /tmp/macs.list
cat /tmp/iwlist.scan | grep Signal\ level= | cut -d = -f 3| cut -d \  -f 1 > /tmp/levels.list
