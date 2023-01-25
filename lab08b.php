<html>
<head>


<style>
table{
width:70%;
background-color: skyblue;

}
tr{

color:red;
}
</style>
</head>

<body>

<?php
$row = $_POST['row'];
$col = $_POST['col'];
$x=0;
if($row < 3 || $row > 12 || $col < 3 || $col > 12)
{

echo "Please adjust your row and column size";

}
else
{
echo "<table border=\"3\" align=\"center\">";
for($i=1 ;  $i <= $row ; $i++)
{
$x++;
echo "<tr >";
$y=$x;
 for($j=1; $j<=$col; $j++)
{

  echo "<td>";
	echo "$y";
echo "</td>";
$y=$y+$x;



}

echo "</tr>";

}




}

?>




















