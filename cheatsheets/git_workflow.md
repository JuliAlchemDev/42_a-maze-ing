# Git Workflow Cheatsheet 🇺🇸

## 1. Branches

Keep `main` stable. Create a branch for each task.

```bash
git switch main
git pull origin main
git switch -c feat/config-parser
```

**Branch naming:**
- `feat/` — new functionality
- `fix/` — bug fixes
- `docs/` — documentation
- `refactor/` — code improvements without changing behavior
- `test/` — tests
- `chore/` — maintenance and tooling

Use short, descriptive names in lowercase, separated by hyphens.

## 2. Conventional Commits

Write commits using this format:

```text
type: short description in imperative form and why
```

Common types:
- `feat:` add functionality
- `fix:` fix a bug
- `docs:` update documentation
- `refactor:` restructure code without changing behavior
- `test:` add or update tests
- `chore:` maintenance, configuration, and tooling

Examples:

```bash
git add config_parser/
git commit -m "feat: add config parser module"
git commit -m "fix: correct PERFECT configuration key"
git commit -m "docs: add virtual environment cheatsheet"
```

Keep commits focused: one logical change per commit.

## 3. Save and Push Changes

Check your working tree before committing:

```bash
git status
git diff
```

Stage only the files related to your task:

```bash
git add path/to/file
git commit -m "type: describe the change"
git push -u origin feat/config-parser
```

For subsequent pushes on the same branch:

```bash
git push
```

## 4. Create a Pull Request (PR)

1. Push your branch to GitHub.
2. Open the repository on GitHub.
3. Select **Compare & pull request** (or open **New pull request**).
4. Set `main` as the base branch and your feature branch as the compare branch.
5. Add a clear title and describe what changed, why, and how you tested it.
6. Review the diff and create the PR.
7. Ask your teammate to review it.

## 5. After the PR Is Merged

Update your local `main` and remove the finished branch:

```bash
git switch main
git pull origin main
git branch -d feat/config-parser
```

If you need to work on another task, create a new branch from the updated `main`.

## Quick Rules

- Never commit directly to `main`.
- Use one branch per task or feature.
- Keep commits small and meaningful.
- Review the diff before creating a PR.
- Communicate with your teammate before merging overlapping changes.
- Do not commit `.venv/`, secrets, or generated files.

--- 

# Flujo de trabajo con Git y GitHub 🇪🇸

## 1. Crear una rama

Mantén `main` estable. Cada tarea se trabaja en su propia rama.

```bash
git switch main
git pull origin main
git switch -c feat/config-parser
```

Prefijos recomendados para las ramas:

- `feat/`: nuevas funcionalidades.
- `fix/`: correcciones.
- `docs/`: documentación.
- `refactor/`: reorganización del código.
- `test/`: pruebas.
- `chore/`: tareas de mantenimiento.

## 2. Crear commits

Utiliza el formato de **Conventional Commits**:

```text
tipo: descripción breve del cambio
```

Tipos habituales:

- `feat`: añadir una funcionalidad.
- `fix`: corregir un error.
- `docs`: actualizar la documentación.
- `refactor`: reorganizar el código sin cambiar su comportamiento.
- `test`: añadir o modificar pruebas.
- `chore`: tareas de mantenimiento.

Ejemplos:

```text
feat: add config parser to load project settings
fix: correct misspelled PERFECT key in config
docs: add virtual environment setup cheatsheet
```

Es recomendable que la descripción sea breve y explique qué ha cambiado. Si necesitas explicar por qué, puedes añadir un cuerpo al commit.

## 3. Guardar y subir los cambios

```bash
git status
git diff
git add <archivo>
git commit -m "tipo: descripción del cambio"
git push -u origin <nombre-rama>
```

- `git status`: consulta el estado de los archivos.
- `git diff`: revisa los cambios antes de guardarlos.
- `git add`: prepara los archivos para el commit.
- `git commit`: guarda los cambios en el historial.
- `git push`: sube los cambios a GitHub.

## 4. Crear una Pull Request (PR)

1. Abre el repositorio en GitHub.
2. Crea una Pull Request desde tu rama hacia `main`.
3. Describe los cambios y las pruebas realizadas.
4. Pide a tu compañero/a que revise el código.
5. Resuelve los comentarios y espera la aprobación antes de integrar los cambios.

## 5. Después de integrar los cambios

Actualiza tu rama local `main` y elimina la rama de la tarea cuando ya no la necesites.

```bash
git switch main
git pull origin main
git branch -d feat/config-parser
```

## Buenas prácticas

- No trabajes directamente en `main`.
- Crea una rama por tarea.
- Haz commits pequeños y centrados en un único cambio.
- Revisa los cambios antes de cada commit.
- Coordínate con tus compañeros si vais a modificar los mismos archivos.
- No subas `.venv`, contraseñas, secretos ni archivos generados que no deban versionarse.
