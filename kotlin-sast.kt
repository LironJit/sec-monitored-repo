// non-vulnerable code

fun main(args : Array<String>) {
    println("Hello, World!")
}

val sql = "INSERT INTO user (username, password) VALUES ('$username', '$password');"

var qry:String="INSERT INTO users (username, password) VALUES('"+username.text.toString()+"','"+password.text.toString()+"')";

var qry:String="SELECT * FROM users WHERE username='"+username.text.toString()+"'";

val cipher = Cipher.getInstance("TripleDES/CBC/PKCS5Padding")
