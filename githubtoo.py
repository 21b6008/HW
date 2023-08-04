<?php
require 'config.php';
if(isset($_SESSION["id"])){
    header("Location: index.php");
}

if(isset($_POST["submit"])){
    $Email = $_POST["email"];
    $Password = $_POST["password"];
    $captcha = $_POST["captcha"];
    $confirmcaptcha = $_POST["confirmcaptcha"];

    if($captcha != $confirmcaptcha){
        echo "<script> alert('Incorrect Captcha'); </script>";
    }
    else{
        $row = mysqli_fetch_assoc(mysqli_query($conn, "SELECT * FROM user WHERE email = $Email"));
        if(isset($row) && $Password == $row["password"]){
            $_SESSION["ID"] = $row["ID"];
            header("Location: index.php");
        }
        else{
            echo "<script> alert('Wrong Password or Email'); </script>";
        }
    }
}
?>