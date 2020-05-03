import java.sql.Connection;
import java.sql.DriverManager;


/**
*
* @author Vladimir Petukhov
* 
*/
public class DB {	
	public static Connection getConnection(){
		Connection con=null;
		try{
			Class.forName("com.mysql.cj.jdbc.Driver");
			con=DriverManager.getConnection("jdbc:mysql://localhost:3306/test","user","password");
		}catch(Exception e){System.out.println(e);}
		return con;
	}

}
