interface IPlayable
{
    void Play();
}

class VideoPlayer : IPlayable
{
    public void Play()
    {
        Console.WriteLine("Playing video");
    }
}

class AudioPlayer : IPlayable
{
    public void Play()
    {
        Console.WriteLine("Playing audio");
    }
}

IPlayable player1 = new VideoPlayer();
IPlayable player2 = new AudioPlayer();
player1.Play();
player2.Play();
