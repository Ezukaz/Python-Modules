Imagine a large construction project.

At the top is the NexusManager, acting as the general contractor — the company responsible for overseeing the entire build. It plans the work, decides the order of tasks, and tells everyone what to do. It doesn’t worry about how workers were hired or trained. When it’s time to work, it simply gives instructions and expects results.

Working under it is the Main Company (ABC), a traditional, structured company. They send their own full-time employees — people like JSONAdapter, CSVAdapter, and StreamAdapter. These workers are officially trained, contract-bound, and must meet strict requirements before they’re even allowed on site. If they don’t meet the standards, they’re not allowed to participate at all.

At the same time, there’s another source of workers: the Hiring Agency (Protocol).

This agency works very differently. Instead of hiring and training people, it simply posts a requirement:

“If you can do process(), you qualify.”

Independent workers — like InputStage, TransformStage, and OutputStage — see this and show up on their own. These are freelancers, similar to solo contractors who work independently rather than belonging to a company. They don’t sign formal contracts with strict rules, and they don’t inherit from any shared structure. They just already have the necessary skill.

The agency doesn’t actively manage them. It simply acts as a shared label — a way of saying, “these workers meet the requirement.” This label helps group them together and allows problems to be caught early (like during type checking), but once the work begins, the agency itself disappears from the picture.

On the construction site, the general contractor (NexusManager) brings everything together.

It doesn’t care:

whether a worker came from the structured company (ABC), or
whether they’re an independent freelancer recognized by the agency (Protocol).

It simply gives the instruction: “do your job (process()).”

If the worker can do it, the system works.

Each ProcessingPipeline is like a specific part of the construction process — a clearly defined workflow:

InputStage brings in materials
TransformStage works on them
OutputStage delivers the finished result

The pipeline ensures everything happens in the right order, step by step.

In the end, the project succeeds because it combines two different approaches:

ABC (inheritance): strict, explicit, and enforced
Protocol (duck typing): flexible, skill-based, and implicit

And tying it all together is the general contractor:

It doesn’t care where a worker came from — only that they can do the job when asked.