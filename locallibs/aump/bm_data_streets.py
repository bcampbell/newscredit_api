#
#   bm_data_streets.py
#
#   David Janes
#   2005.04.19
#
#	Information about street names
#

# src: http://www.usps.com/ncsc/lookups/usps_abbreviations.html
street_map = {
	"alley" : "Alley",
	"ally" : "Alley",
	"aly" : "Alley",
	"allee" : "Alley",
	"anex" : "Annex",
	"annex" : "Annex",
	"annx" : "Annex",
	"anx" : "Annex",
	"arc" : "Arcade",
	"arcade" : "Arcade",
	"av" : "Avenue",
	"ave" : "Avenue",
	"aven" : "Avenue",
	"avenu" : "Avenue",
	"avenue" : "Avenue",
	"avn" : "Avenue",
	"avnue" : "Avenue",
	"bayoo" : "Bayoo",
	"bayou" : "Bayoo",
	"bch" : "Beach",
	"beach" : "Beach",
	"bend" : "Bend",
	"bnd" : "Bend",
	"blf" : "Bluff",
	"bluf" : "Bluff",
	"bluff" : "Bluff",
	"bluffs" : "Bluffs",
	"bot" : "Bottom",
	"bottm" : "Bottom",
	"bottom" : "Bottom",
	"btm" : "Bottom",
	"blvd" : "Boulevard",
	"boul" : "Boulevard",
	"boulevard" : "Boulevard",
	"boulv" : "Boulevard",
	"br" : "Branch",
	"branch" : "Branch",
	"brnch" : "Branch",
	"brdge" : "Bridge",
	"brg" : "Bridge",
	"bridge" : "Bridge",
	"brk" : "Brook",
	"brook" : "Brook",
	"brooks" : "Brooks",
	"burg" : "Burg",
	"burgs" : "Burgs",
	"byp" : "Bypass",
	"bypa" : "Bypass",
	"bypas" : "Bypass",
	"bypass" : "Bypass",
	"byps" : "Bypass",
	"camp" : "Camp",
	"cmp" : "Camp",
	"cp" : "Camp",
	"canyn" : "Canyon",
	"canyon" : "Canyon",
	"cnyn" : "Canyon",
	"cyn" : "Canyon",
	"cape" : "Cape",
	"cpe" : "Cape",
	"causeway" : "Causeway",
	"causway" : "Causeway",
	"cswy" : "Causeway",
	"cen" : "Center",
	"cent" : "Center",
	"center" : "Center",
	"centr" : "Center",
	"centre" : "Center",
	"cnter" : "Center",
	"cntr" : "Center",
	"ctr" : "Center",
	"centers" : "Centers",
	"cir" : "Circle",
	"circ" : "Circle",
	"circl" : "Circle",
	"circle" : "Circle",
	"crcl" : "Circle",
	"crcle" : "Circle",
	"circles" : "Circles",
	"clf" : "Cliff",
	"cliff" : "Cliff",
	"clfs" : "Cliffs",
	"cliffs" : "Cliffs",
	"clb" : "Club",
	"club" : "Club",
	"common" : "Common",
	"cor" : "Corner",
	"corner" : "Corner",
	"corners" : "Corners",
	"cors" : "Corners",
	"course" : "Course",
	"crse" : "Course",
	"court" : "Court",
	"crt" : "Court",
	"ct" : "Court",
	"courts" : "Courts",
	"ct" : "Courts",
	"cove" : "Cove",
	"cv" : "Cove",
	"coves" : "Coves",
	"ck" : "Creek",

	# "cr" : "Creek", -- changed by dpj 2005.12.31
	"cr" : "Crescent",

	"creek" : "Creek",
	"crk" : "Creek",
	"crecent" : "Crescent",
	"cres" : "Crescent",
	"crescent" : "Crescent",
	"cresent" : "Crescent",
	"crscnt" : "Crescent",
	"crsent" : "Crescent",
	"crsnt" : "Crescent",
	"crest" : "Crest",
	"crossing" : "Crossing",
	"crssing" : "Crossing",
	"crssng" : "Crossing",
	"xing" : "Crossing",
	"crossroad" : "Crossroad",
	"curve" : "Curve",
	"dale" : "Dale",
	"dl" : "Dale",
	"dam" : "Dam",
	"dm" : "Dam",
	"div" : "Divide",
	"divide" : "Divide",
	"dv" : "Divide",
	"dvd" : "Divide",
	"dr" : "Drive",
	"driv" : "Drive",
	"drive" : "Drive",
	"drv" : "Drive",
	"drives" : "Drives",
	"est" : "Estate",
	"estate" : "Estate",
	"estates" : "Estates",
	"ests" : "Estates",
	"exp" : "Expressway",
	"expr" : "Expressway",
	"express" : "Expressway",
	"expressway" : "Expressway",
	"expw" : "Expressway",
	"expy" : "Expressway",
	"ext" : "Extension",
	"extension" : "Extension",
	"extn" : "Extension",
	"extnsn" : "Extension",
	"extensions" : "Extensions",
	"exts" : "Extensions",
	"fall" : "Fall",
	"falls" : "Falls",
	"fls" : "Falls",
	"ferry" : "Ferry",
	"frry" : "Ferry",
	"fry" : "Ferry",
	"field" : "Field",
	"fld" : "Field",
	"fields" : "Fields",
	"flds" : "Fields",
	"flat" : "Flat",
	"flt" : "Flat",
	"flats" : "Flats",
	"flts" : "Flats",
	"ford" : "Ford",
	"frd" : "Ford",
	"fords" : "Fords",
	"forest" : "Forest",
	"forests" : "Forest",
	"frst" : "Forest",
	"forg" : "Forge",
	"forge" : "Forge",
	"frg" : "Forge",
	"forges" : "Forges",
	"fork" : "Fork",
	"frk" : "Fork",
	"forks" : "Forks",
	"frks" : "Forks",
	"fort" : "Fort",
	"frt" : "Fort",
	"ft" : "Fort",
	"freeway" : "Freeway",
	"freewy" : "Freeway",
	"frway" : "Freeway",
	"frwy" : "Freeway",
	"fwy" : "Freeway",
	"garden" : "Garden",
	"gardn" : "Garden",
	"gdn" : "Garden",
	"grden" : "Garden",
	"grdn" : "Garden",
	"gardens" : "Gardens",
	"gdns" : "Gardens",
	"grdns" : "Gardens",
	"gateway" : "Gateway",
	"gatewy" : "Gateway",
	"gatway" : "Gateway",
	"gtway" : "Gateway",
	"gtwy" : "Gateway",
	"glen" : "Glen",
	"gln" : "Glen",
	"glens" : "Glens",
	"green" : "Green",
	"grn" : "Green",
	"greens" : "Greens",
	"grov" : "Grove",
	"grove" : "Grove",
	"grv" : "Grove",
	"groves" : "Groves",
	"harb" : "Harbor",
	"harbor" : "Harbor",
	"harbr" : "Harbor",
	"hbr" : "Harbor",
	"hrbor" : "Harbor",
	"harbors" : "Harbors",
	"haven" : "Haven",
	"havn" : "Haven",
	"hvn" : "Haven",
	"height" : "Heights",
	"heights" : "Heights",
	"hgts" : "Heights",
	"ht" : "Heights",
	"hts" : "Heights",
	"highway" : "Highway",
	"highwy" : "Highway",
	"hiway" : "Highway",
	"hiwy" : "Highway",
	"hway" : "Highway",
	"hwy" : "Highway",
	"hill" : "Hill",
	"hl" : "Hill",
	"hills" : "Hills",
	"hls" : "Hills",
	"hllw" : "Hollow",
	"hollow" : "Hollow",
	"hollows" : "Hollow",
	"holw" : "Hollow",
	"holws" : "Hollow",
	"inlet" : "Inlet",
	"inlt" : "Inlet",
	"is" : "Island",
	"island" : "Island",
	"islnd" : "Island",
	"islands" : "Islands",
	"islnds" : "Islands",
	"iss" : "Islands",
	"isle" : "Isle",
	"isles" : "Isle",
	"jct" : "Junction",
	"jction" : "Junction",
	"jctn" : "Junction",
	"junction" : "Junction",
	"junctn" : "Junction",
	"juncton" : "Junction",
	"jctns" : "Junctions",
	"jcts" : "Junctions",
	"junctions" : "Junctions",
	"key" : "Key",
	"ky" : "Key",
	"keys" : "Keys",
	"kys" : "Keys",
	"knl" : "Knoll",
	"knol" : "Knoll",
	"knoll" : "Knoll",
	"knls" : "Knolls",
	"knolls" : "Knolls",
	"lake" : "Lake",
	"lk" : "Lake",
	"lakes" : "Lakes",
	"lks" : "Lakes",
	"land" : "Land",
	"landing" : "Landing",
	"lndg" : "Landing",
	"lndng" : "Landing",
	"la" : "Lane",
	"lane" : "Lane",
	"lanes" : "Lane",
	"ln" : "Lane",
	"lgt" : "Light",
	"light" : "Light",
	"lights" : "Lights",
	"lf" : "Loaf",
	"loaf" : "Loaf",
	"lck" : "Lock",
	"lock" : "Lock",
	"lcks" : "Locks",
	"locks" : "Locks",
	"ldg" : "Lodge",
	"ldge" : "Lodge",
	"lodg" : "Lodge",
	"lodge" : "Lodge",
	"loop" : "Loop",
	"loops" : "Loop",
	"mall" : "Mall",
	"manor" : "Manor",
	"mnr" : "Manor",
	"manors" : "Manors",
	"mnrs" : "Manors",
	"mdw" : "Meadow",
	"meadow" : "Meadow",
	"mdws" : "Meadows",
	"meadows" : "Meadows",
	"medows" : "Meadows",
	"mews" : "Mews",
	"mill" : "Mill",
	"ml" : "Mill",
	"mills" : "Mills",
	"mls" : "Mills",
	"mission" : "Mission",
	"missn" : "Mission",
	"msn" : "Mission",
	"mssn" : "Mission",
	"motorway" : "Motorway",
	"mnt" : "Mount",
	"mount" : "Mount",
	"mt" : "Mount",
	"mntain" : "Mountain",
	"mntn" : "Mountain",
	"mountain" : "Mountain",
	"mountin" : "Mountain",
	"mtin" : "Mountain",
	"mtn" : "Mountain",
	"mntns" : "Mountains",
	"mountains" : "Mountains",
	"nck" : "Neck",
	"neck" : "Neck",
	"orch" : "Orchard",
	"orchard" : "Orchard",
	"orchrd" : "Orchard",
	"oval" : "Oval",
	"ovl" : "Oval",
	"overpass" : "Overpass",
	"park" : "Park",
	"pk" : "Park",
	"prk" : "Park",
	"parks" : "Parks",
	"parkway" : "Parkway",
	"parkwy" : "Parkway",
	"pkway" : "Parkway",
	"pkwy" : "Parkway",
	"pky" : "Parkway",
	"parkways" : "Parkways",
	"pkwys" : "Parkways",
	"pass" : "Pass",
	"passage" : "Passage",
	"path" : "Path",
	"paths" : "Path",
	"pike" : "Pike",
	"pikes" : "Pike",
	"pine" : "Pine",
	"pines" : "Pines",
	"pnes" : "Pines",
	"pl" : "Place",
	"place" : "Place",
	"plain" : "Plain",
	"pln" : "Plain",
	"plaines" : "Plains",
	"plains" : "Plains",
	"plns" : "Plains",
	"plaza" : "Plaza",
	"plz" : "Plaza",
	"plza" : "Plaza",
	"point" : "Point",
	"pt" : "Point",
	"points" : "Points",
	"pts" : "Points",
	"port" : "Port",
	"prt" : "Port",
	"ports" : "Ports",
	"prts" : "Ports",
	"pr" : "Prairie",
	"prairie" : "Prairie",
	"prarie" : "Prairie",
	"prr" : "Prairie",
	"rad" : "Radial",
	"radial" : "Radial",
	"radiel" : "Radial",
	"radl" : "Radial",
	"ramp" : "Ramp",
	"ranch" : "Ranch",
	"ranches" : "Ranch",
	"rnch" : "Ranch",
	"rnchs" : "Ranch",
	"rapid" : "Rapid",
	"rpd" : "Rapid",
	"rapids" : "Rapids",
	"rpds" : "Rapids",
	"rest" : "Rest",
	"rst" : "Rest",
	"rdg" : "Ridge",
	"rdge" : "Ridge",
	"ridge" : "Ridge",
	"rdgs" : "Ridges",
	"ridges" : "Ridges",
	"riv" : "River",
	"river" : "River",
	"rivr" : "River",
	"rvr" : "River",
	"rd" : "Road",
	"road" : "Road",
	"rds" : "Roads",
	"roads" : "Roads",
	"route" : "Route",
	"row" : "Row",
	"rue" : "Rue",
	"run" : "Run",
	"shl" : "Shoal",
	"shoal" : "Shoal",
	"shls" : "Shoals",
	"shoals" : "Shoals",
	"shoar" : "Shore",
	"shore" : "Shore",
	"shr" : "Shore",
	"shoars" : "Shores",
	"shores" : "Shores",
	"shrs" : "Shores",
	"skyway" : "Skyway",
	"spg" : "Spring",
	"spng" : "Spring",
	"spring" : "Spring",
	"sprng" : "Spring",
	"spgs" : "Springs",
	"spngs" : "Springs",
	"springs" : "Springs",
	"sprngs" : "Springs",
	"spur" : "Spur",
	"spurs" : "Spurs",
	"sq" : "Square",
	"sqr" : "Square",
	"sqre" : "Square",
	"squ" : "Square",
	"square" : "Square",
	"sqrs" : "Squares",
	"squares" : "Squares",
	"sta" : "Station",
	"station" : "Station",
	"statn" : "Station",
	"stn" : "Station",
	"stra" : "Stravenue",
	"strav" : "Stravenue",
	"strave" : "Stravenue",
	"straven" : "Stravenue",
	"stravenue" : "Stravenue",
	"stravn" : "Stravenue",
	"strvn" : "Stravenue",
	"strvnue" : "Stravenue",
	"stream" : "Stream",
	"streme" : "Stream",
	"strm" : "Stream",
	"st" : "Street",
	"str" : "Street",
	"street" : "Street",
	"strt" : "Street",
	"streets" : "Streets",
	"smt" : "Summit",
	"sumit" : "Summit",
	"sumitt" : "Summit",
	"summit" : "Summit",
	"ter" : "Terrace",
	"terr" : "Terrace",
	"terrace" : "Terrace",
	"throughway" : "Throughway",
	"trace" : "Trace",
	"traces" : "Trace",
	"trce" : "Trace",
	"track" : "Track",
	"tracks" : "Track",
	"trak" : "Track",
	"trk" : "Track",
	"trks" : "Track",
	"trafficway" : "Trafficway",
	"trfy" : "Trafficway",
	"tr" : "Trail",
	"trail" : "Trail",
	"trails" : "Trail",
	"trl" : "Trail",
	"trls" : "Trail",
	"tunel" : "Tunnel",
	"tunl" : "Tunnel",
	"tunls" : "Tunnel",
	"tunnel" : "Tunnel",
	"tunnels" : "Tunnel",
	"tunnl" : "Tunnel",
	"tpk" : "Turnpike",
	"tpke" : "Turnpike",
	"trnpk" : "Turnpike",
	"trpk" : "Turnpike",
	"turnpike" : "Turnpike",
	"turnpk" : "Turnpike",
	"underpass" : "Underpass",
	"un" : "Union",
	"union" : "Union",
	"unions" : "Unions",
	"valley" : "Valley",
	"vally" : "Valley",
	"vlly" : "Valley",
	"vly" : "Valley",
	"valleys" : "Valleys",
	"vlys" : "Valleys",
	"vdct" : "Viaduct",
	"via" : "Viaduct",
	"viadct" : "Viaduct",
	"viaduct" : "Viaduct",
	"view" : "View",
	"vw" : "View",
	"views" : "Views",
	"vws" : "Views",
	"vill" : "Village",
	"villag" : "Village",
	"village" : "Village",
	"villg" : "Village",
	"villiage" : "Village",
	"vlg" : "Village",
	"villages" : "Villages",
	"vlgs" : "Villages",
	"ville" : "Ville",
	"vl" : "Ville",
	"vis" : "Vista",
	"vist" : "Vista",
	"vista" : "Vista",
	"vst" : "Vista",
	"vsta" : "Vista",
	"walk" : "Walk",
	"walks" : "Walks",
	"wall" : "Wall",
	"way" : "Way",
	"wy" : "Way",
	"ways" : "Ways",
	"well" : "Well",
	"wells" : "Wells",
	"wls" : "Wells",
}
