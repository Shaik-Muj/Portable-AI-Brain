import { useState } from "react";
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import PromptEditor from "./components/PromptEditor";
import ResponseViewer from "./components/ResponseViewer";

const MODELS = ["openai", "ollama", "llama", "gemma"];

function App() {
  const [prompt, setPrompt] = useState("");
  const [responses, setResponses] = useState<Record<string, string>>({});
  const [selectedModels, setSelectedModels] = useState<string[]>(MODELS);
  const [loadingModels, setLoadingModels] = useState<string[]>([]);

  const handleToggleModel = (model: string) => {
    setSelectedModels((prev) =>
      prev.includes(model)
        ? prev.filter((m) => m !== model)
        : [...prev, model]
    );
  };

  const handlePromptSubmit = async () => {
    if (!prompt.trim()) return;

    setResponses({});
    setLoadingModels([...selectedModels]);

    await Promise.all(
      selectedModels.map(async (model) => {
        try {
          const res = await fetch("http://localhost:8000/prompt", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt, model }),
          });

          const data = await res.json();
          setResponses((prev) => ({ ...prev, [model]: data.response }));
        } catch (error) {
          setResponses((prev) => ({
            ...prev,
            [model]: `Error: ${(error as Error).message}`,
          }));
        } finally {
          setLoadingModels((prev) => prev.filter((m) => m !== model));
        }
      })
    );
  };

  return (
    <div className="min-h-screen flex flex-col bg-gray-100">
      <Header />
      <div className="flex flex-1">
        <Sidebar
          models={MODELS}
          selectedModels={selectedModels}
          onToggle={handleToggleModel}
        />
        <main className="flex-1 p-4 space-y-4">
          <PromptEditor
            prompt={prompt}
            setPrompt={setPrompt}
            onSubmit={handlePromptSubmit}
          />
          <ResponseViewer
            responses={responses}
            loadingModels={loadingModels}
          />
        </main>
      </div>
    </div>
  );
}

export default App;
