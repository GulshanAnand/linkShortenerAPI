import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Map;
import java.util.HashMap;
import java.util.Iterator;

public class test {
    public static void main(String[] args) throws IOException {
        URL url = new URL("http://localhost:5000/shorten");
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        connection.setDoOutput(true);

        Map<String, String> formFields = new HashMap<>();
        formFields.put("url", "https://www.github.com");

        StringBuilder postData = new StringBuilder();
        for (Map.Entry<String, String> param : formFields.entrySet()) {
            if (postData.length() != 0) {
                postData.append('&');
            }
            postData.append(param.getKey());
            postData.append('=');
            postData.append(param.getValue());
        }

        byte[] postDataBytes = postData.toString().getBytes("UTF-8");
        connection.getOutputStream().write(postDataBytes);

        BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        System.out.println("Response status code: " + connection.getResponseCode());
        System.out.println("Response body: " + response.toString());
    }
}
