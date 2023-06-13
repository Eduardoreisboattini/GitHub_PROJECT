async Task<string> DownloadContentAsync(string url)
{
    HttpClient client = new HttpClient();
    string content = await client.GetStringAsync(url);
    return content;
}

string url = "https://example.com";
string result = await DownloadContentAsync(url);
Console.WriteLine(result);