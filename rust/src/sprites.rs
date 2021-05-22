// extern crate sdl2; 

// use std::time::Duration;
use std::fs::{DirEntry, File, read_dir};
use std::error;
use std::io;
use std::env::current_dir;
// use std::io::prelude::*;
use std::path::Path;
// use strum::AsStaticRef;


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


impl ActionImages {
    fn new(name: String, path: &'static Path) -> ActionImages {
        ActionImages {
            name: name,
            path: path,
        }
    }
}

fn get_file_list(path: &Path) -> Result<(), io::Error> {
    let path = current_dir()?.as_path().join(path);
    println!("path: {:?}", path);
    for entry in read_dir(path)? {
        let entry = entry?;
        println!("entry: {:?}", entry);
    }
    Ok(())
}

/* Create an ActionImages from an assesst directory.
 * The directory is expected to have one-or-more of
 * each of the action frames.
 */
// XXX - 'from string' seems wrong for this.  Maybe from path instead.
// impl From<&str> for ActionImages {
//     fn from(s: &str) -> Result<ActionImages, Box<dyn error::Error>> {


//         // Open directory
//         let path = Path::new(s);
//         println!("path = {:?}", path);
//         let mut file = match File::open(&path) {
//             Err(why) => panic!("couldn't open {}: {}", path.display(), why),
//             Ok(file) => file,
//         };
//         ActionImages {
//             name: "Idle".into(),
//             source: s.into()
//         }
//     }
// }



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
        if get_file_list(path).is_err() {
            println!("{}", get_file_list(path).unwrap_err());
        }
    }


}