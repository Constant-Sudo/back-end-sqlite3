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
    classes!: [number];

    @Column()
    email!: [string];
}

Teacher - id, surname, name, classes, email