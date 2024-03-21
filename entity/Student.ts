import { Entity, Column, PrimaryGeneratedColumn } from "typeorm"

@Entity()
export class Exams {
    @PrimaryGeneratedColumn()
    id!: number;

    @Column()
    vorname!: string;

    @Column()
    nachname!: string;

    @Column()
    class!: number;

    @Column()
    teachers!: [number];

    @Column()
    parents_mail!: string;

    @Column()
    exams!: [number];

    @Column()
    personal_rating!: [{
        rating: [number],
        comment: string,
    }];
}



Teacher - id, surname, name, classes, email
Students - id, surname, name, class, teachers, parents_mail, exams, personal_rating