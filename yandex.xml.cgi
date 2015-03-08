<ya_lbs_request>
<common>
<version>1.0</version>
<api_key>AF5JN04BAAAA6whOMAIAptyIlZNT6pC1ijdFN15KhMbuUI8AAAAAAAAAAAC9Kr9D83HCh5c-F_y-VhjnjiTN5w==</api_key>
</common>
<wifi_networks>
<?$i=0; $macs = fopen("/tmp/macs.list", "r"); $levels = fopen("/tmp/levels.list", "r") >
<? while(!feof($macs) && !feof($levels)) >
<? $i++; $mac = fgets($macs,255); $level = fgets($levels,255) >
<network><mac><? echo $mac></mac><signal_strength><? echo $level></signal_strength><age><? echo $i*10+1000 ></age></network>
<? endwhile >
</wifi_networks>
</ya_lbs_request>
