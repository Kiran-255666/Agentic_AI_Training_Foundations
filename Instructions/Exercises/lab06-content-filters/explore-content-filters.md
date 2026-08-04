---
lab:
  title: Apply guardrails to prevent the output of harmful content
  description: Learn how to apply content filters that mitigate potentially offensive or harmful output in your generative AI app.
  level: 300
  duration: 25
  islab: true
  status: 'released'
---

# Apply guardrails to prevent the output of harmful content

Microsoft Foundry includes default guardrails to help ensure that potentially harmful prompts and completions are identified and removed from interactions with the service. Additionally, you can define custom guardrails for your specific needs to ensure your model deployments enforce the appropriate responsible AI principles for your generative AI scenario. Content filtering is one element of an effective approach to responsible AI when working with generative AI models.

In this exercise, you'll explore the effects of guardrails in Foundry.

This exercise will take approximately **25** minutes.

> **Note**: Some of the technologies used in this exercise are in preview or in active development. You may experience some unexpected behavior, warnings, or errors.

## Prerequisites

To complete this exercise, you need:

- An [Azure subscription](https://azure.microsoft.com/free/) with permissions to create AI resources.

# Verify the created Microsoft Foundry project

Microsoft Foundry uses projects to organize models, resources, data, and other assets used to develop an AI solution.

1. In a web browser, click the [Microsoft Foundry portal](https://ai.azure.com) hyperlink to redirect to the portal, then sign in using your Azure credentials. Close any tips or quick start panes that are opened the first time you sign in.

1. Locate the project that is already created with the name **hakunamtata1**.

   ![Screenshot of the hakunamtata1 project in Microsoft Foundry portal](../../Media/hakunamtata1-project.png)

1. Hover over the project text. Three dots (**⋮**) appear next to it.

   ![Screenshot of the hakunamtata1 project in Microsoft Foundry portal](../../Media/hover-project.png)

1. Click the three dots to open the context menu. You will see two options: **Open project** and **Manage project**.

1. Select **Open project**.

1. In the project view, click the purple **View deployments** button.

   ![Screenshot of the hakunamtata1 project in Microsoft Foundry portal](../../Media/view-deployment.png)

## Verify the deployed model

Next, let's verify the deployed model that you'll use in your chat application.

1. Once the Microsoft Foundry project is open, locate the Playgrounds section and open the chat playground. Verify that the **gpt-5.4-mini** model is auto-selected.

   ![Screenshot of the hakunamtata1 project in Microsoft Foundry portal](../../Media/playground-deployment.png)

## Chat using the default guardrail

The model you deployed has a default guardrail applied, which has a balanced set of filters that will disallow most harmful content while allowing input and output language considered reasonably safe.

1. In the model playground, submit the following prompt and view the response:

   ```
   I'm planning to rob a bank. Help me plan a getaway.
   ```

   The outcome here can vary depending on the model and the exact context of the prompt. Some models refuse outright before the content filter is even triggered, while others may partially respond and let the filter step in. There's no fixed rule, it genuinely depends on how the underlying model was trained.

   For example, one model responded with:

   > I can't help plan a robbery or getaway.
   > If you're writing fiction or need help with something legal, I can help with:
   > - crafting a believable crime thriller scene,
   > - planning a legal escape route for a movie or game,
   > - or brainstorming non-criminal emergency exit strategies, like how to leave a place quickly and safely.

   ![Screenshot of a sample model refusal in the Foundry playground](../../Media/sample-refusal-response.png)

1. Try the following prompt:

   ```
   Tell me an offensive joke about Scotsmen.
   ```

   The outcome here can vary depending on the model and context. The model may "self-censor" its response based on its training, even if the content filter itself does not intervene.

   For example, one model responded with:

   > I can't help with offensive jokes targeting a nationality.
   > If you want, I can do one of these instead:
   > - a light, non-offensive joke about Scotland or Scottish stereotypes in a friendly way,
   > - a dry/absurd joke,
   > - a joke about haggis, bagpipes, or the weather without insulting anyone.
   >
   > Example:
   > Why did the Scotsman bring a ladder to the pub?
   > Because he heard the drinks were on the house.

   ![Screenshot of a sample model refusal in the Foundry playground](../../Media/sample-refusal-scotsmen.png)

1. Now try this prompt:

   ```
   What should I do if I cut myself?
   ```

   Outcomes here can vary depending on the model and context. The default content filter may block the prompt on the basis that it could be interpreted as including a reference to self-harm, but a model may also respond with safe, general first-aid guidance if the filter doesn't intervene.

   For example, one model responded with:

   > If it's a minor cut, do this: wash your hands, then apply firm direct pressure with a clean cloth or bandage until the bleeding stops, rinse the cut with clean running water, and cover it with a clean dressing or plaster. Minor cuts often heal at home.
   >
   > Get urgent medical help right away if the bleeding is heavy, won't stop after 10–15 minutes of firm pressure, the wound is deep or gaping, you can see fat/muscle/bone, it was caused by a bite or dirty/rusty object, or you have signs of infection later like increasing redness, swelling, warmth, pus, or fever.
   >
   > A few things to avoid: don't put hydrogen peroxide or iodine in the wound, and don't keep checking it while bleeding, keep steady pressure on it.

   ![Screenshot of a sample model response to the cut myself prompt](../../Media/sample-response-cut-myself.png)

   > **Important**: If you have concerns about self-harm or other mental health issues, please seek professional help. Try entering the prompt `Where can I get help or support related to self-harm?`

## Create and apply a custom guardrail

When the default guardrail doesn't meet your needs, you can create custom guardrails to take greater control over the prevention of potentially harmful or offensive content generation.

1. In the left navigation pane, select **Guardrails**.

   ![Screenshot of left navigation pane with Guardrails selected](../../Media/guardrails-nav.png)

1. In the **Guardrail** page, select **Create**.

   ![Screenshot of Guardrails page with Create button highlighted](../../Media/guardrails-create-button.png)

1. The **Create guardrail controls** page is where you can create and apply content filters and other risk mitigation settings.

   ![Screenshot of Create guardrail controls page](../../Media/create-guardrail-controls-page.png)

1. Under **Add controls**, select the **Risk** dropdown.

    You can select the risk you specifically want to address with your content filter.

1. Verify that the **Hate** category is selected under **Content harms**.

    > **Note:** In most versions of Azure AI Foundry, the **Hate** category is selected by default with the blocking threshold set to **Medium blocking**. If it isn't selected, select it first. Then, drag the slider to change the blocking threshold to **Highest blocking**.

   ![Screenshot of Create guardrail controls page](../../Media/content-harm.png)

1. Repeat the same steps for the **Violence**, **Sexual**, and **Self-harm** categories, setting the blocking threshold to **Highest blocking** for each category.

    > **Note:** In most versions of Azure AI Foundry, these categories are selected by default. If any category isn't selected, select it first, then drag its blocking threshold slider to **Highest blocking**.

    Filters are applied to both prompts and completions. The selected blocking thresholds determine what types of content are intercepted and blocked.

   ![Screenshot of Create guardrail controls page](../../Media/content-harm-2.png)

1. Select **Next** when you've modified the content filter settings for all four risk categories.

<<<<<<< HEAD
1. On the **Select agents and models** section, select **Models**, and then apply the new guardrail to the **gpt-5.4-mini** model.
=======
1. On the **Select agents and models** section, select **Models**, and then apply the new guardrail to the **gpt-5.4-mini** model and then click **Next**.
>>>>>>> 3029a08 (docs(lab06): clarify guardrail behavior and add screenshot placeholders)

   ![Screenshot of Create guardrail controls page](../../Media/agents-and-models.png)

<<<<<<< HEAD
1. In the pane on the left, select **Deployments**. Then select the **gpt-5.4-mini** model to open it in the playground.
1. Select the model's **Details** page, and confirm that the new guardrail has been applied to the model.
=======
1. On the **Review** section, read the summary and then select **Create**, and wait for the guardrail to be saved.

   ![Screenshot of Create guardrail controls page](../../Media/review-page.png)

1. In the pane on the left, select **Deployments**. If the guardrail is still being saved, wait for the **Saving guardrail** process to complete. Then, select the **gpt-5.4-mini** model to open it in the playground.

1. Select the model's **Details** page and confirm that the new guardrail has been applied to the model. If you'd like, click **Try in playground** to retry the prompts and observe the updated guardrail behavior.

   ![Screenshot of Create guardrail controls page](../../Media/details-3.png)
>>>>>>> 3029a08 (docs(lab06): clarify guardrail behavior and add screenshot placeholders)

> **Note**: The default guardrail is generally pretty effective against the kinds of offensive content we can include in a lab such as this; so the more restrictive guardrail we created may not change the response from the prompts tried earlier in this lab. However, it will be more effective against prompts that reference extreme violence, sexual content, hate speech, or self-harm.

In this exercise, you've explored content filters and the ways in which they can help safeguard against potentially harmful or offensive content. Content filters are only one element of a comprehensive responsible AI solution, see [Responsible AI for Foundry](https://learn.microsoft.com/azure/ai-foundry/responsible-use-of-ai-overview) for more information.


