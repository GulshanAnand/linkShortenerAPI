import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class test {

    public static void main(String[] args) throws IOException {

        // Create a new URL object
        URL url = new URL("https://labwired.tech/shorten");

        // Open a connection to the URL
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();

        // Set the request method to POST
        connection.setRequestMethod("POST");

        // Set the content type to JSON
        connection.setRequestProperty("Content-Type", "application/json");

        // Enable output for the connection
        connection.setDoOutput(true);

        // Create a JSON payload
        String jsonPayload = "{\"url\":\"https://www.python.org\",\"alias\":\"j\"}";

        // Write the JSON payload to the connection's output stream
        OutputStream outputStream = connection.getOutputStream();
        outputStream.write(jsonPayload.getBytes());
        outputStream.flush();
        outputStream.close();

        // Read the response from the server
        BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        String line;
        StringBuilder responseBuilder = new StringBuilder();
        while ((line = reader.readLine()) != null) {
            responseBuilder.append(line);
        }
        reader.close();

        // Print the response from the server
        String response = responseBuilder.toString();
        System.out.println(response);
    }
}
