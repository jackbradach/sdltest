
// use std::time::Duration;
use std::fs::{DirEntry, File, ReadDir, read_dir};
use std::error;
use std::io;
use std::env::current_dir;
// use std::io::prelude::*;
use std::path::{Path,PathBuf};
// use strum::AsStaticRef;

extern crate sdl2;
use sdl2::image::LoadSurface;

enum Action {
    Attack,
    Fall,
    Hit,
    Hurt,
    Idle,
    Jump,
    PickUp,
    Pull,
    Push,
    SAttack,
    Walk,
    Wave
}

struct ActionImages {
    name: String,
    path: &'static Path
    // action: Action,
}

/*
    Hashmap<name, Vec<Surface>>

*/

/* Create an ActionImages from an assesst directory.
 * The directory is expected to have one-or-more of
 * each of the action frames.
 */
impl ActionImages {
    fn new(name: String, path: &'static Path) -> ActionImages {
        ActionImages {
            name: name,
            path: path,
        }
    }
}

/* Get an iterator of DirEntry (eg, a ReadDir) instances for the contents
 * of the given path.
 * 
 * Returns io::Errs for a bad directory, otherwise all valid images found
 * get returned in a Vec<PathBuf>.
 */
// TODO - make this return validated File objects.
fn get_actionimages_file_list(path: &Path) -> io::Result<Vec<PathBuf>> {
    let path = current_dir()?.as_path().join(path);
    let entries = read_dir(path)?;
    Ok(entries.filter_map(|s| Some(s.ok().unwrap().path().to_path_buf())).collect())
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_actionimages_from_string() {
        // Pass in string to asset directory, should return an ActionImages object.
        let path = Some(Path::new("assests/assassin")).unwrap();
        let assassin = ActionImages::new("assassin".to_string(), path);
        assert_eq!(assassin.name, "assassin".to_string());
        // assert_eq!(assassin.action, Action::Idle);
        if get_actionimages_file_list(path).is_err() {
            println!("{}", get_actionimages_file_list(path).unwrap_err());
        }
    }


}