<?php

$h = date('H'); // it will return hour in 24 format.


if ($h >= 0 && $h <= 12)
{
 $img = 'morning.webp';
$message= "Good morning";
} 
    else if ($h >= 12 && $h < 18) 
{
$img="afternoon.jpg";
$message= "Good Afternoon";
} 
    else if ($h >= 18 && $h <= 21) 
{
$img = 'evening.jpg';
$message= "Good evening";
} 
else if ($h >= 21 && $h < 24) 
{ 
$img = 'night.webp';
$message= "Good night";
}
$total_count = 0;
if(isset($_COOKIE['count'])){
$total_count = $_COOKIE['count'];
$total_count ++;
}
setcookie('count', $total_count);



?>
<html>
<head>
<style type="text/css">
body
{
background-image: url('<?php echo $img;?>');
  background-repeat: no-repeat;
  background-attachment: fixed;  
  background-size: cover;
text-align : center;
color: white;

}

.p1{
	text-align : center;
	color : white;
	font-size : 50px;

}
img
{

position: absolute;
  top: 20px;
  right: 16px;
 opacity: 0.8;
}
</style>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

</head>
<body>
<?php if (isset ($_GET['image'])) { $result=$_GET['image']; ?>
<img src="<?php echo $result; ?>">
<p style="color:red; position:relative;"> <?php echo " Halloween image is $result"; ?>  </p>
<?php } ?>
<p class="p1"> <?php echo $message; ?> </p>
 <form action="lab08b.php" method="POST" id="form" name="form" onsubmit="return validate()">
    <div>
      <h1>Enter two Integers from 3 to 12</h1>
      <br>
    </div>

    <b>Number of Rows (3 to 12):</b> <input type="text" id = "ROW" name="row" placeholder="3-12">
    <br>
    <b>Number of Columns (3 to 12):</b><input type="text" id = "COL" name="col" placeholder="3-12">
    <br>
    <input class="button-primary" type="submit" value="Submit">
    <br>
    </form>

<p style="position: absolute; bottom: 10px; font-size: 20px; color: antiquewhite"> <?php echo "You have viewed this page $total_count times" ?> </p>


</body>
</html>