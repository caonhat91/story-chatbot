export async function streamChat(payload: unknown, onMessage: (t: string) => void, signal?: AbortSignal) {
  const res = await fetch(import.meta.env.VITE_API_URL + "/chat/stream", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
    signal
  });

  const reader = res.body!.getReader();
  const decoder = new TextDecoder("utf-8");

  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    onMessage(decoder.decode(value));
  }
}
