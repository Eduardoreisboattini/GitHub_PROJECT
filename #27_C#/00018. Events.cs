class Button
{
    public event EventHandler Click;

    public void OnClick()
    {
        Click?.Invoke(this, EventArgs.Empty);
    }
}

void HandleClick(object sender, EventArgs e)
{
    Console.WriteLine("Button clicked");
}

Button button = new Button();
button.Click += HandleClick;
button.OnClick();
