# reNEVADA360
A recompilation of Fallout New Vegas (USA) + Ultimate Edition using ReXGlue SDK

## Logo of recomp:
<img width="1280" height="720" alt="photo_2026-09-08_10-44-52" src="https://github.com/user-attachments/assets/0e0633b2-402d-493e-acfb-7627d68a1e2c" />


## How does the project work?

We are using the latest version of the ReXGlue SDK (08/09/26 - 0.10.0) to recompile the game, utilizing its tools, Ghidra 12, and Visual Studio 2026 + Developer Command Prompt.

*Current progress (08/09/26)*
<img width="1920" height="1032" alt="Reprodutor Multimídia 07_09_2026 21_25_51" src="https://github.com/user-attachments/assets/7b39a416-db55-468a-98a5-2beead1c253c" />
You can't see the image clearly, but it shows the game launching for the first time after fixing the SDK Kernel/FileSystem and enabling Xenos in the project.
It's still in the very early stages, so I'll only release an .exe much later, once there's something at least minimally playable.You can't see the image clearly, but it shows the game launching for the first time after fixing the SDK Kernel/FileSystem and enabling Xenos in the project.
It's still in the very early stages, so I'll only release an .exe much later, once there's something at least minimally playable.

## Future of project:

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:

```mermaid
sequenceDiagram
Recomp ->> New port: C++ 
New port ->> Android/Switch: arm64
Recomp ->> New Render/Jolt Physics: Better experience
```

It’s still very early days, and it will take a while for things to get done, but we’ll get there eventually. If you’re interested, take a look at this other project where *Fallout: New Vegas* is being ported to the Godot Engine: https://github.com/nikamigaming-create/OpenNV

## Licence:
I released the project under the MIT license—I don't know much about licenses—and there are no game assets included, only ReXGlue content. If you want to play it later, make sure you have your own complete US copy of the game, okay?
