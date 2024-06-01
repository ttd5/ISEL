import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;

/**
 * This class represents a simple web client that communicates with a web server using TCP sockets.
 * It sends an HTTP GET request to the server and processes the HTTP response.
 *
 * Author: Tatiana Damaya
 */
public class WebClientPhase1 {

    /**
     * The main method of the WebClientPhase1 class.
     * It establishes a TCP connection with the server, sends an HTTP GET request,
     * receives the HTTP response, and processes it.
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        // Server address and port
        String serverAddress = "127.0.0.1"; // Replace with the server's IP address
        int serverPort = 80;

        try (
            // Establish TCP connection with the server
            Socket socket = new Socket(serverAddress, serverPort);
            // Output stream to send data to the server
            PrintWriter out = new PrintWriter(new OutputStreamWriter(socket.getOutputStream()), true);
            // Input stream to receive data from the server
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))
        ) {
        	// Send an HTTP GET request to the server
        	out.print("GET / HTTP/1.1\r\n"); // Request line with the GET method and HTTP version
        	out.print("Host: " + serverAddress + "\r\n"); // Host header
        	out.print("Connection: close\r\n"); // Indicates that the connection will be closed after the response
        	out.print("\r\n"); // Blank line indicating the end of headers
        	out.flush(); // Flushes the buffer and sends the data immediately

            // Receive and process the HTTP response from the server
            StringBuilder responseBuilder = new StringBuilder();
            String line;
            while ((line = in.readLine()) != null) {
                responseBuilder.append(line).append("\n");
            }
            String response = responseBuilder.toString();

            // Print the HTTP response
            System.out.println("Response from server (" + serverAddress + "):" + "\n");
            System.out.println(response);

            // Interpret the HTTP status code and handle the response
            int statusCode = extractStatusCode(response);
            handleResponse(statusCode);

        } catch (Exception e) {
            // Print any exceptions that occur during the execution
            e.printStackTrace();
        }
    }

    /**
     * Extracts the HTTP status code from the response.
     * @param response The HTTP response string.
     * @return The HTTP status code.
     */
    private static int extractStatusCode(String response) {
        // Split the response into lines and extract the first line
        String[] lines = response.split("\n");
        String firstLine = lines[0].trim();
        // Split the first line by whitespace and extract the status code
        String[] parts = firstLine.split("\\s+");
        return Integer.parseInt(parts[1]);
    }

    /**
     * Handles the HTTP response based on the status code.
     * @param statusCode The HTTP status code.
     */
    private static void handleResponse(int statusCode) {
        // Act based on the HTTP status code
        switch (statusCode) {
            case 200:
                System.out.println("Request successful");
                break;
            case 301:
                System.out.println("Moved Permanently");
                break;
            case 302:
                System.out.println("Found");
                break;
            case 400:
                System.out.println("Bad Request");
                break;
            case 401:
                System.out.println("Unauthorized");
                break;
            case 403:
                System.out.println("Forbidden");
                break;
            case 404:
                System.out.println("Not Found");
                break;
            case 500:
                System.out.println("Internal Server Error");
                break;
            case 503:
                System.out.println("Service Unavailable");
                break;
            default:
                System.out.println("Unexpected response code: " + statusCode);
        }
    }
}
