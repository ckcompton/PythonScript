 Import-Module MariaDBCmdlets




$User="root"
$Password="football12"
$Database="testdb2"
$Server="localhost"
$Port=3306


while(1){
$password2=""
$hex = (1..16 | %{ '{0:X}' -f (Get-Random -Max 16) }) -join ''
$hex = '0x' + $hex

# slv_sbx_asp
$alphas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
for ($i = 0; $i -lt 4; $i++) {
		$password2 += (Get-Random -InputObject $alphas).ToLower()
	}

$sum_time = get-random -minimum 0 -Maximum 100000
$min_time = get-random -minimum 0 -Maximum 10000
$max_time = get-random -minimum 0 -Maximum 80000
if($sum_time -lt ($min_time+$max_time)){
$sum_time = $min_time+$max_time
}
if(($min_time -lt 5000) -or ($max_time -lt 5000)){
$sum_time=0
$min_time=0
$max_time=0
}
$sum_time
$min_time
$max_time

$digest_text=""

$queriesList = ('select','where','RANDOM',' CREATE TABLE testtable(hostgroup INT, schemaname VARCHAR(240) NOT NULL, username VARCHAR(240) NOT NULL, client_address VARCHAR(240), digest VARCHAR(255) NOT NULL, digest_text TEXT, count_star INT, first_seen INT, last_seen INT,sum_time INT, min_time INT, max_time INT);','nt from zb_state','group on','AS NEXT','DELETE ALL','as count()','SELECT m.name AS name, m.label AS label, m.field_type AS field_type, m.field_index AS field_index, m.field_length AS field_length, m.required AS required','SELECT time_zone FROM zb_tenant WHERE id=?')
for ($i = 0; $i -lt 3; $i++){
		$digest_text += (Get-Random -InputObject $queriesList)
	}
"Digest Text LEnght" + $digest_text.Length

$usernameDB = "slv_${password2}_asp"
$usernameDB
$username
$mariadb = Connect-MariaDB  -User $User -Password $Password -Database $Database -Server $Server -Port $Port
$data = Invoke-MariaDB -Connection $mariadb -Query "INSERT INTO testtable(hostgroup,schemaname,username,digest,digest_text,count_star,first_seen,last_seen,sum_time,min_time,max_time,client_address) VALUES (1,'myapps02','$usernameDB','$hex','$digest_text',1,1663943165,1663943165,$sum_time,$min_time,$max_time,'');"
$data

Start-Sleep -Seconds 30


} 
