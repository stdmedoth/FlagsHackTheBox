for id in $( seq 1 1) 
do
	response=$(curl -v -L --request POST --url http://10.10.10.239/login.php --header 'Content-Type: multipart/form-data; boundary=---011000010111000001101001' --cookie PHPSESSID=pe9qh1qrids8ndji87i9qmi39b --form voter=1234 --form password=1234 --form login=1)

  	echo $response;
  	#erro=$(echo $response | grep "Cannot find voter with the ID")
  	#echo $erro;
done
